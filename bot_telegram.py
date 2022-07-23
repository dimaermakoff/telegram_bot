import sqlite3 as sq
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot
import sqlite_db
from sqlite_db import sql_start
from create_bot import dp,bot 



	
storage=MemoryStorage()


async def on_startup(_):
	sqlite_db.sql_start()

#Кнопки клавиатуры админа
button_load = KeyboardButton('/✅Завантаж-Овочевий')
button_load1 = KeyboardButton('/✅Завантаж-Фруктовий')
button_load2 = KeyboardButton('/✅Завантаж-Ковбасний')
button_load3 = KeyboardButton('/✅Завантаж-Солодкий')
button_load4 = KeyboardButton('/✅Завантаж-Горіховий')
button_load5 = KeyboardButton('/✅Завантаж-Еко-торбинки')
button_load6 = KeyboardButton('/✅Завантаж-Сухобарвний')
button_load7 = KeyboardButton('/✅Аватарка')
button_delete = KeyboardButton('/🚫Видалити-Овочевий')
button_delete1 = KeyboardButton('/🚫Видалити-Фруктовий')
button_delete2 = KeyboardButton('/🚫Видалити-Ковбасний')
button_delete3 = KeyboardButton('/🚫Видалити-Солодкий')
button_delete4 = KeyboardButton('/🚫Видалити-Горіховий')
button_delete5 = KeyboardButton('/🚫Видалити-Еко-торбинки')
button_delete6 = KeyboardButton('/🚫Видалити-Сухобарвний')
button_delete7 = KeyboardButton('/🚫Видалити-Аватарку')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)
button_case_admin.row(button_load,button_delete).row(button_load1,button_delete1).row(button_load2,button_delete2).row(button_load3,button_delete3).row(button_load4,button_delete4).row(button_load5,button_delete5).row(button_load6,button_delete6).row(button_load7,button_delete7)

ID = None

class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin1(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin2(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin3(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin4(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin5(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin6(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()
class FSMAdmin7(StatesGroup):
	photo = State()
	name = State()

#Получаем ID текущего модератора
@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_change_command(message: types.Message):
	global ID 
	ID = message.from_user.id
	await bot.send_message(message.from_user.id, 'Что хозяйка надо⁉', reply_markup=button_case_admin)
	await message.delete()

                          #НАЧАЛО диалога загрузки нового пункта МЕНЮ!
@dp.message_handler(commands='✅Завантаж-Овочевий',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin.photo.set()
		await message.reply('Завантаж фото овочевого')
#1
@dp.message_handler(commands='✅Завантаж-Фруктовий',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin1.photo.set()
		await message.reply('Завантаж фото фруктового')
#2	
@dp.message_handler(commands='✅Завантаж-Ковбасний',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin2.photo.set()
		await message.reply('Завантаж фото ковбасного')
#3
@dp.message_handler(commands='✅Завантаж-Солодкий',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin3.photo.set()
		await message.reply('Завантаж фото солодкого')
#4
@dp.message_handler(commands='✅Завантаж-Горіховий',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin4.photo.set()
		await message.reply('Завантаж фото горіхового')
#5		
@dp.message_handler(commands='✅Завантаж-Еко-торбинки',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin5.photo.set()
		await message.reply('Завантаж фото Еко-торбинки')
#6
@dp.message_handler(commands='✅Завантаж-Сухобарвний',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin6.photo.set()
		await message.reply('Завантаж фото сухобарвного')
#7
@dp.message_handler(commands='✅Аватарка',state=None)
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin7.photo.set()
		await message.reply('Завантаж Аватарку')
	

                       #Ловим  первый ответ и пишем словарь НАЗВАНИЕ!
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.reply("Тепер введи назву")
#1
@dp.message_handler(content_types=['photo'], state=FSMAdmin1.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin1.next()
		await message.reply("Тепер введи назву")
#2
@dp.message_handler(content_types=['photo'], state=FSMAdmin2.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin2.next()
		await message.reply("Тепер введи назву")
#3
@dp.message_handler(content_types=['photo'], state=FSMAdmin3.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin3.next()
		await message.reply("Тепер введи назву")
#4
@dp.message_handler(content_types=['photo'], state=FSMAdmin4.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin4.next()
		await message.reply("Тепер введи назву")
#5
@dp.message_handler(content_types=['photo'], state=FSMAdmin5.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin5.next()
		await message.reply("Тепер введи назву")
#6
@dp.message_handler(content_types=['photo'], state=FSMAdmin6.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin6.next()
		await message.reply("Тепер введи назву")
#7
@dp.message_handler(content_types=['photo'], state=FSMAdmin7.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin7.next()
		await message.reply("Тепер введи назву")

                               #Ловим второй ответ ОПИСАНИЕ!
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin.next()	
		await message.reply("Введи опис букету")
#1
@dp.message_handler(state=FSMAdmin1.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin1.next()	
		await message.reply("Введи опис букету")
#2
@dp.message_handler(state=FSMAdmin2.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin2.next()	
		await message.reply("Введи опис букету")
#3
@dp.message_handler(state=FSMAdmin3.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin3.next()	
		await message.reply("Введи опис букету")
#4
@dp.message_handler(state=FSMAdmin4.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin4.next()	
		await message.reply("Введи опис букету")
#5
@dp.message_handler(state=FSMAdmin5.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin5.next()	
		await message.reply("Введи опис торбинки")
#6
@dp.message_handler(state=FSMAdmin6.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin6.next()	
		await message.reply("Введи опис букету")
#7
@dp.message_handler(state=FSMAdmin7.name)
async def load_name(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await sqlite_db.sql_add_command7(state)
		await state.finish()

									#Ловит третий ответ ЦЕНА!!!!

@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin.next()
		await message.reply("Тепер вкажи ціну")
#1
@dp.message_handler(state=FSMAdmin1.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin1.next()
		await message.reply("Тепер вкажи ціну")
#2
@dp.message_handler(state=FSMAdmin2.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin2.next()
		await message.reply("Тепер вкажи ціну")
#3
@dp.message_handler(state=FSMAdmin3.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin3.next()
		await message.reply("Тепер вкажи ціну")
#4
@dp.message_handler(state=FSMAdmin4.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin4.next()
		await message.reply("Тепер вкажи ціну")
#5
@dp.message_handler(state=FSMAdmin5.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin5.next()
		await message.reply("Тепер вкажи ціну")

#6
@dp.message_handler(state=FSMAdmin6.description)
async def load_description(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin6.next()
		await message.reply("Тепер вкажи ціну")

			# Ловим последний ответ и используем полученнные ДАННЫЕ!!!float()- только цифры
@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command(state)
		await state.finish()
#1
@dp.message_handler(state=FSMAdmin1.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command1(state)
		await state.finish()
#2
@dp.message_handler(state=FSMAdmin2.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command2(state)
		await state.finish()
#3
@dp.message_handler(state=FSMAdmin3.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command3(state)
		await state.finish()
#4
@dp.message_handler(state=FSMAdmin4.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command4(state)
		await state.finish()
#5
@dp.message_handler(state=FSMAdmin5.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command5(state)
		await state.finish()
#6
@dp.message_handler(state=FSMAdmin6.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db.sql_add_command6(state)
		await state.finish()

		


						# Удаление позиций из базы ДАННЫХ!!!!

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Овочевий')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'🚫Видалити-Овочевий {ret[1]}', callback_data=f'del {ret[1]}')))
#1
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Фруктовий')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete1()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'🚫Видалити-Фруктовий {ret[1]}', callback_data=f'del {ret[1]}')))
#2
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Ковбасний')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete2()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'🚫Видалити-Ковбасний {ret[1]}', callback_data=f'del {ret[1]}')))
#3
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Солодкий')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete3()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'🚫Видалити-Солодкий {ret[1]}', callback_data=f'del {ret[1]}')))
#4
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Горіховий')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete4()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'🚫Видалити-Горіховий {ret[1]}', callback_data=f'del {ret[1]}')))
#5
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Еко-торбинки')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete5()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
add(InlineKeyboardButton(f'🚫Видалити-Еко-торбинки {ret[1]}', callback_data=f'del {ret[1]}')))
#6
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ","")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Сухобарвний')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete6()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
			await bot.send_message(message.from_user.id, text='🔼🔼🔼', reply_markup=InlineKeyboardMarkup().\
add(InlineKeyboardButton(f'🚫Видалити-Сухобарвний {ret[1]}', callback_data=f'del {ret[1]}')))
#7
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del'))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del'))
	await callback_query.answer(text=f'{callback_query.data.replace("del")} Видалено❗', show_alert=True)

@dp.message_handler(commands='🚫Видалити-Аватарку')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_delete7()
		for ret in read:
			await bot.send_photo(message.from_user.id,ret[0])
			await bot.send_message(message.from_user.id, text='🔼🔼🔼',reply_markup=InlineKeyboardMarkup().\
add(InlineKeyboardButton(f'🚫Видалити-Аватарку {ret[1]}', callback_data=f'del {ret[1]}')))

b1 = KeyboardButton('/Овочевий🥑')
b2 = KeyboardButton('/Фруктовий🥑')
b3 = KeyboardButton('/Ковбасний🥑')
b4 = KeyboardButton('/Солодкий🥑')
b5 = KeyboardButton('/Горіховий🥑')
b6 = KeyboardButton('/Еко-торбинки🥑')
b7 = KeyboardButton('/Сухобарвний🥑')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1,b2).row(b3,b4).row(b5,b6).add(b7)

@dp.message_handler(commands=['start' , 'help'])
async def command_start(message : types.Message):
	try:
		await sqlite_db.sql_read7(message)
		await bot.send_message(message.from_user.id, 'Вітаю,хочешь замовити смачний букет?\nЯ флорист Ліліана.\nУ цьому боті Ви можете подивитись каталог букетів\nДля замовлення зателефонуй або напиши💌 у Телеграм/Вайбер за номером +380733097990' , reply_markup=kb_client)
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


executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
