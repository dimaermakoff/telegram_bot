from aiogram import types,Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db,sqlite_db1,sqlite_db2, sqlite_db3,sqlite_db4,sqlite_db5


@dp.message_handler(commands=['start' , 'help'])
async def command_start(message : types.Message):
	try:
		await sqlite_db.sql_read7(message)
		await bot.send_message(message.from_user.id,'Вітаю,хочешь замовити смачний букет?\nЯ флорист Ліліана.\nУ цьому боті Ви можете подивитись каталог букетів\nДля замовлення зателефонуй або напиши💌 у Телеграм/Вайбер за номером +380733097990' , reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Спілкування с ботом через ЛС, напишіть йому:\nhttps//t.me/masterskaya_avokado_zpBot')

@dp.message_handler(commands=['Овочевий🥑'])
async def byket_open_command(message : types.Message):
	await sqlite_db.sql_read(message)

@dp.message_handler(commands=['Фруктовий🥑'])
async def byket_place_command(message : types.Message):
	await sqlite_db.sql_read1(message)

@dp.message_handler(commands=['Ковбасний🥑'])
async def byket_vait_command(message : types.Message):
	await sqlite_db.sql_read2(message)

@dp.message_handler(commands=['Солодкий🥑'])
async def byket_state_command(message : types.Message):
	await sqlite_db.sql_read3(message)

@dp.message_handler(commands=['Горіховий🥑'])
async def byket_mait_command(message : types.Message):
	await sqlite_db.sql_read4(message)
	
@dp.message_handler(commands=['Еко-торбинки🥑'])
async def byket_save_command(message : types.Message):
	await sqlite_db.sql_read5(message)

@dp.message_handler(commands=['Сухобарвний🥑'])
async def byket_save_command(message : types.Message):
	await sqlite_db.sql_read6(message)
		

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(byket_open_command, commands=['Овочевий🥑'])
    dp.register_message_handler(byket_vait_command, commands=['Ковбасний🥑'])
    dp.register_message_handler(byket_place_command, commands=['Фруктовий🥑'])													