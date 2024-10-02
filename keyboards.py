from aiogram import types


def start_keyboard():
    pass


def registration():
    buttons = [
        [
            types.InlineKeyboardButton(text="10", callback_data="10"),
            types.InlineKeyboardButton(text="11", callback_data="11")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
