import aiohttp
import horoscope
import time
import logging
from aiogram import Bot, Dispatcher, executor, types


# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w", \
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "{}, choose an action:"

bot = Bot("6150613668:AAE-R7v3TvaQoK_EQRBMxHs_t9EpElnnwRg")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Привет, {user_full_name}!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=4)
    btn_calc = types.KeyboardButton('/telegram_chanal')
    btn_notes = types.KeyboardButton('/horoscope')
    btn_image = types.KeyboardButton('/send_image')
    btn_out = types.KeyboardButton('/quit')
    btns.add(btn_calc, btn_notes, btn_image, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)


@dp.message_handler(commands=['telegram_chanal'])
async def quit_handler(message: types.Message):
    text = 'https://t.me/Artem_2011_hockey'
    await bot.send_message(message.from_user.id, text,
                           reply_markup=types.ReplyKeyboardRemove())
@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Goodbye! See you...',
                           reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['horoscope'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите дату рождения в формате dd.mm.yyyy: ',
                           reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: types.Message):
    list = horoscope.zadiak_info(message.text)
    list1 = 'По году Вы -'+list[0] +'; по месяцу - ' + list[1]
    await bot.send_message(message.from_user.id, list1,
                            reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['send_image'])
async def cmd_send_image(message):
    with open("hock.jpg", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)


if __name__ == '__main__':
    executor.start_polling(dp)
