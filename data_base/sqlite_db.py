import sqlite3 as sq
from create_bot import bot


def sql_start():
	global base, cur 
	base = sq.connect('База Данных.db')
	cur = base.cursor()
	if base:
		print('Data base connected OK!')
	base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
	base.commit()


async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_read(message):
	for ret in cur.execute('SELECT * FROM menu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read1(message):
	for ret in cur.execute('SELECT * FROM venu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read2(message):
	for ret in cur.execute('SELECT * FROM fenu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read3(message):
	for ret in cur.execute('SELECT * FROM eenu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read4(message):
	for ret in cur.execute('SELECT * FROM renu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read5(message):
	for ret in cur.execute('SELECT * FROM aenu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read6(message):
	for ret in cur.execute('SELECT * FROM сenu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
async def sql_read7(message):
	for ret in cur.execute('SELECT * FROM henu').fetchall():
		await bot.send_photo(message.from_user.id, ret[0])

async def sql_delete():
	return cur.execute('SELECT * FROM menu').fetchall()
async def sql_delete1():
	return cur.execute('SELECT * FROM venu').fetchall()
async def sql_delete2():
	return cur.execute('SELECT * FROM fenu').fetchall()
async def sql_delete3():
	return cur.execute('SELECT * FROM eenu').fetchall()
async def sql_delete4():
	return cur.execute('SELECT * FROM renu').fetchall()
async def sql_delete5():
	return cur.execute('SELECT * FROM aenu').fetchall()
async def sql_delete6():
	return cur.execute('SELECT * FROM cenu').fetchall()
async def sql_delete7():
	return cur.execute('SELECT * FROM henu').fetchall()

		
async def sql_delete_command(data):
	cur.execute('DELETE FROM menu WHERE name == ?',(data,))
	cur.execute('DELETE FROM venu WHERE name == ?',(data,))
	cur.execute('DELETE FROM fenu WHERE name == ?',(data,))
	cur.execute('DELETE FROM eenu WHERE name == ?',(data,))
	cur.execute('DELETE FROM renu WHERE name == ?',(data,))
	cur.execute('DELETE FROM aenu WHERE name == ?',(data,))
	cur.execute('DELETE FROM сenu WHERE name == ?',(data,))
	cur.execute('DELETE FROM henu WHERE name == ?',(data,))
	base.commit()

