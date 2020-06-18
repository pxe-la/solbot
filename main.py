COOLDOWN = 10 * 60;
TEXT = '''
Привет, это бар Соль.

У нас работает балкон и внутренний двор. Несложная схема прохода висит на двери бара.

Мы не бронирем столики  на балконе и отключили доставку через телеграм. Заказать доставку можно в Яндексе и Delivery Club.

Если вдруг все столики на балконе заняты, то к вашим услугам мы подготовили большой двор с минибаром и кухней.

Работаем ежедневно с 11 дня до 3 ночи.
'''

from pyrogram import Client, Filters
from storage import PersistJSON

storage = PersistJSON("config.json");
print(storage);
app = Client("my_account")

chat_timers = {};

@app.on_message(Filters.chat('me'))
def onoff(client, message):
    if message.text == 'bot.start':
        storage['enabled'] = True;
        message.reply_text('Bot enabled');
    elif message.text == 'bot.stop':
        storage['enabled'] = False;
        message.reply_text('Bot disabled');
    elif message.text == 'bot.status':
        message.reply_text('enabled' if storage.enabled else 'disabled');
    elif message.text.startswith('bot.cooldown'):
        storage.cooldown = int(message.text.split[' '][1]);
        message.reply('Ok, now cooldown time: {} seconds '.format(storage.cooldown));
    elif message.text.startswith('bot.message'):
        storage.message = message.text.split(' ', 1)[1];
        message.reply('Ok, message:');
        message.reply(storage.message);

@app.on_message(Filters.text)
def autoReply(client, message):
    if not storage['enabled']:
        return;
    if (message.chat.id not in chat_timers) or (message.date - chat_timers[message.chat.id] > storage.cooldown):
        chat_timers[message.chat.id] = message.date;
        message.reply_text(storage.message);

app.run();
