from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db,sqlite_db1,sqlite_db2,sqlite_db3,sqlite_db4,sqlite_db5,sqlite_db6,sqlite_db7
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
	await bot.send_message(message.from_user.id, 'Что хозяйка надо⁉', reply_markup=admin_kb.button_case_admin)
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
		await FSMAdmin5.photo.set()
		await message.reply('Завантаж фото сухобарвного')

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
		await sqlite_db7.sql_add_command(state)
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

		await sqlite_db1.sql_add_command(state)
		await state.finish()
#2
@dp.message_handler(state=FSMAdmin2.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db2.sql_add_command(state)
		await state.finish()
#3
@dp.message_handler(state=FSMAdmin3.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db3.sql_add_command(state)
		await state.finish()
#4
@dp.message_handler(state=FSMAdmin4.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db4.sql_add_command(state)
		await state.finish()
#5
@dp.message_handler(state=FSMAdmin5.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db5.sql_add_command(state)
		await state.finish()
#6
@dp.message_handler(state=FSMAdmin6.price)
async def load_price(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = message.text

		await sqlite_db6.sql_add_command(state)
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


		


#Вход из состояния
##@dp.message_handler(state="*", commands='отмена')
##@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
##async def cancel_handler(message: types.Message, state:FSMContext):
###	if message.from_user.id == ID:
#		current_state = await state.get_state()
#			return
#		await state.finish()
#		await message.reply('OK')

#Регистрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)	
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_description, state=FSMAdmin.description)
	dp.register_message_handler(load_price, state=FSMAdmin.price)
	#dp.register_message_handler(cancel_handler, state="*", commands='отмена')
	#dp.register_message_handler(cancel_handler, Text(equals='отмена',ignore_case=True), state="*")
	dp.register_message_handler(make_change_command, commands=['moderator'], is_chat_admin=True)	