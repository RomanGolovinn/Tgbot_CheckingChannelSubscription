from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Показать каналы'), KeyboardButton(text='Проверить подписки')]
    ]
)

channels = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Канал1', url='t.me/channel1testsubchecking')],
        [InlineKeyboardButton(text='Канал2', url='t.me/channel2testsubchecking')],
        [InlineKeyboardButton(text='Канал3', url='t.me/channel3testsubchecking')]
    ]
)
