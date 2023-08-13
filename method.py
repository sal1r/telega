from util import make_query
from type import *
from typing import List

async def send_message(session, token, chat_id: int, text: str) -> bool:
    data = {
        'chat_id': chat_id,
        'text': text
    }

    resp = await make_query(session, token, 'sendMessage', data)
    return resp['ok']

async def get_updates(session, token, offset: int = 0, timeout: int = 0) -> List[Update]:
    data = {
        'offset': offset,
        'timeout': timeout
        }

    resp = await make_query(session, token, 'getUpdates', data)
    print(resp)
    updates = []

    for upd in resp.get('result'):
        mess = upd.get('message')
        if mess:
            ch = mess.get('chat')
            chat = Chat(id=ch.get('id'), type=ch.get('type'))
            text = mess.get('text')
            photo = mess.get('photo')
            if photo:
                photo = photo[len(photo)-1].get('file_id')
            
            message = Message(id=mess.get('message_id'), text=text,
                              chat=chat, photo=photo)
        updates.append(Update(id=upd.get('update_id'), message=message))
    
    return updates
