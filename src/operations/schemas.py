from typing import Optional

from pydantic import BaseModel


class SMovieAdd(BaseModel):
    name: str
    description: Optional[str] = None
    category: str


class SMovie(SMovieAdd):
    id: int

class SMovieId(BaseModel):
    ok: bool = True
    movie_id: int