
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db, sqlite_db1,sqlite_db2, sqlite_db3,sqlite_db4,sqlite_db5,sqlite_db6,sqlite_db7


async def on_startup(_):
	print('Бот вышел онлайн')
	sqlite_db.sql_start()
	sqlite_db1.sql_start()
	sqlite_db2.sql_start()
	sqlite_db3.sql_start()
	sqlite_db4.sql_start()
	sqlite_db5.sql_start()
	sqlite_db6.sql_start()
	sqlite_db7.sql_start()
	

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True , on_startup=on_startup)
