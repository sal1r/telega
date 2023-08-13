import aiohttp

async def make_query(session: aiohttp.ClientSession, token: str, 
                     method: str, data: dict = None) -> dict:
    return await (await session.get(f'/bot{token}/{method}', params=data)).json()

async def download_file(session: aiohttp.ClientSession, token: str, file_id: str):
    resp = await make_query(session, token, 'getFile', {'file_id':file_id})
    path = resp.get('result').get('file_path')
    return await (await session.get(f'/file/bot{token}/{path}')).read()