from sqlalchemy import select

from database import new_session, MoviesOrm
from schemas import SMovieAdd, SMovie


class MovieRepository:
    @classmethod
    async def add_one(cls, data: SMovieAdd) -> int:
        async with new_session() as session:
            movie_dict = data.model_dump()

            movie = MoviesOrm(**movie_dict)
            session.add(movie)
            await session.flush()
            await session.commit()
            return movie.id

    @classmethod
    async def find_all(cls) -> list[SMovie]:
        async with new_session() as session:
            query = select(MoviesOrm)
            result = await session.execute(query)
            movie_models = result.scalars().all()
            movie_schemas = [SMovie.model_validate(movie_model) for movie_model in movie_models]
            return movie_schemas