from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

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
#row. incert