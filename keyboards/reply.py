from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGUAGES


def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton(text="Перевод"),
        KeyboardButton(text="История")
    )
    return kb

def lang_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True ,one_time_keyboard=True)
    buttons = []
    for lang in LANGUAGES.values():
        buttons.append(KeyboardButton(text=lang))

    kb.add(*buttons)
    return kb

def continue_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(
        KeyboardButton('Да'),
        KeyboardButton('Нет')
    )
    return kb