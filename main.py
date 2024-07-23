from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as router_manager



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Clean')
    await create_tables()
    print('Ready')
    yield
    print('Off')


app = FastAPI(lifespan=lifespan)
app.include_router(router_manager)
