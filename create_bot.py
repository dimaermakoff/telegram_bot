from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = '5542785678:AAFx4K8qVleVYLRuKBbOZqGwGLQUxSZiriw'
storage=MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)