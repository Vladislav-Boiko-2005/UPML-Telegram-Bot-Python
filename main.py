import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

from config_reader import config
from app.text import text_data
from user_info import nuw_user
import keyboards

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер для бота
dp = Dispatcher()


# Хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    with suppress(TelegramBadRequest):
        await message.answer(text_data['start'], reply_markup=keyboards.registration())


# Хендлер на регистрацию пользователя
@dp.callback_query(F.data == '10')
@dp.callback_query(F.data == '11')
async def user_info(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    user_class = callback.data
    nuw_user(user_id, username, user_class)
    await callback.answer(text_data['callback_user'])


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
