from aiogram import Bot
from aiogram.enums.chat_member_status import ChatMemberStatus

channels = ['@channel1testsubchecking', '@channel2testsubchecking', '@channel3testsubchecking']

async def is_user_subscribed(bot: Bot, user_id: int) -> bool:
    for channel in channels:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status == ChatMemberStatus.LEFT:
                return False
        except Exception as e:
            print(f"Ошибка при проверке подписки: {e}")
            return False
    return True