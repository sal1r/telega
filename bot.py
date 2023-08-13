import asyncio
import aiohttp
from method import *
from type import *
from state_machine import *
import time
from typing import cast
from util import *

class Bot:
	def __init__(self, token: str, timeout: int = 0) -> None:
		self.token = token
		self.handlers = []
		self.offset = 0
		self.timeout = timeout

	async def start_polling(self):
		self.session = aiohttp.ClientSession('https://api.telegram.org')
		
		while True:
			updates = await get_updates(self.session, self.token, self.offset, self.timeout)
			for update in updates:
				self.offset = update.id + 1
				for func in self.handlers:
					await func(update.message)
	
	async def send(self, chat_id: int, text: str) -> None:
		await send_message(self.session, self.token, chat_id, text)
	
	def message(self, func):
		async def decorator(message: Message, state: StateContext | None = None):
			args = cast(dict, func.__annotations__)
			args.pop('return', 0)

			match len(args):
				case 1:
					await func(message)
				case 2:
					await func(message, state)
				case _:
					raise RuntimeError(f"Invalid args count: {len(args)}")

		self.handlers.append(decorator)
		return decorator

	# ЗАСУНУТЬ КУДА-ТО
	async def df(self, id):
		return await download_file(self.session, self.token, id)

	def __del__(self):
		asyncio.ensure_future(self.session.close())
