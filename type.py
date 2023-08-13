from dataclasses import dataclass

@dataclass
class Chat:
	id: int
	type: str
	title: str | None = None
	username: str | None = None
	first_name: str | None = None
	last_name: str | None = None

@dataclass
class User:
	id: int
	is_bot: bool
	first_name: str
	last_name: str | None = None
	username: str | None = None

@dataclass
class Message:
	id: int
	chat: Chat
	from_user: User | None = None
	text: str | None = None
	photo: str | None = None
	dice: int | None = None

@dataclass
class Update:
	id: int
	message: Message | None = None