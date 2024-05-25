import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(
            level=logging.INFO,
            format=('#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                    '%(lineno)d - %(name)s - %(message)s')
        )
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped!")
