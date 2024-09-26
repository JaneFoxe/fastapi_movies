from typing import Annotated

from fastapi import APIRouter, Depends

from src.repository import MovieRepository
from schemas import SMovieAdd, SMovie, SMovieId

router = APIRouter(
    prefix="/movie",
    tags=["Фильмы"],
)


@router.post("")
async def add_movie(
        movie: Annotated[SMovieAdd, Depends()],
) -> SMovieId:
    movie_id = await MovieRepository.add_one(movie)
    return {"ok": True, "movie_id": movie_id}


@router.get("")
async def get_movie() -> list[SMovie]:
    movies = await MovieRepository.find_all()
    return movies

