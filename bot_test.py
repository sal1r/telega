from bot import Bot
from type import Message
from state_machine import *
import asyncio

bot = Bot('6154268713:AAEzV00vGzhFLWNtUjzk5hJqaLo_WGmhhvo', 10)

@bot.message
async def hello(message: Message, state: StateContext) -> None:
	if message.text:
		await bot.send(message.chat.id, message.text)
	
	if message.photo:
		photo = await bot.df(message.photo)
		with open('photo.jpg', 'wb') as file:
			file.write(photo)

loop = asyncio.new_event_loop()
loop.run_until_complete(bot.start_polling())