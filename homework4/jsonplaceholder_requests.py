import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com"

async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_users_data() -> list[dict]:
    return await fetch_json(USERS_DATA_URL)

async def fetch_posts_data() -> list[dict]:
    return await fetch_json(POSTS_DATA_URL)

