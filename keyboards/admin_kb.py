from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



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