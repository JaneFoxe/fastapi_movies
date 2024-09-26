from fastapi import FastAPI
from src.operations.router import router as movie_router


app = FastAPI()
app.include_router(movie_router)



