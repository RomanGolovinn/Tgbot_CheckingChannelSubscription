import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from handlers import router

bot = Bot(token='7948285966:AAFF0fCac-V7LaeYMu13R4Pb3jXrg2mREmA')
dp =Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')