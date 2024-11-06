from data import bot


def main():
    from handlers import commands, texts

    print("bot running")
    bot.infinity_polling()

main()