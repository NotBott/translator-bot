from data import bot
from keyboards.reply import start_kb

@bot.message_handler(commands=["start"])
def start(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, "Добро пожаловать в бот переводчик. Выберите действие ниже", reply_markup=start_kb())
