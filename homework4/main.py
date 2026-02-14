import asyncio
from models import Base, engine, Session, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def add_data_to_db(users_data: list[dict], posts_data: list[dict]):
    async with Session() as session:
        # Создаем объекты моделей
        users = [User(name=u['name'], username=u['username'], email=u['email'], id=u['id']) for u in users_data]
        posts = [Post(user_id=p['userId'], title=p['title'], body=p['body']) for p in posts_data]
        
        session.add_all(users)
        session.add_all(posts)
        await session.commit()

async def async_main():
    await create_tables()
    
    # Конкурентная загрузка данных
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    
    await add_data_to_db(users_data, posts_data)
    await engine.dispose()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()

