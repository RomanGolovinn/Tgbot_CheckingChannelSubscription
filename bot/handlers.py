from aiogram import Router, F
from aiogram.types import Message, ChatJoinRequest
from aiogram.filters import Command

import keyboards as kb
from check_subscription import is_user_subscribed

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет\nДля подписки на этот канал вы должны быть подписаны на эти 3\nНажмите на "Показать каналы", что бы подписаться', reply_markup=kb.main)

@router.message(F.text == 'Показать каналы')
async def show_channels(message: Message):
    await message.answer('Подпишитесь на эти каналы', reply_markup=kb.channels)

@router.message(F.text == 'Проверить подписки')
async def check_subscription(message: Message):
    if await is_user_subscribed(message.bot, message.from_user.id):
        await message.answer("вы подписаны\n Ссылка на вступление: https://t.me/+IdXSXyQgKiE3MTE6")

    else:
        await message.answer('Похоже вы не подписаны\nПодпишитесь на эти каналы:', reply_markup=kb.channels)
