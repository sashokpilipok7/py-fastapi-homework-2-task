from datetime import date
from typing import Optional

from database.models import MovieStatusEnum
from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country_id: int

class MovieDetailSchema(MovieBase):
    pass

class MovieCreate(MovieBase):
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]

class MovieUpdate(MovieBase):
    pass


class MovieListItemSchema(MovieBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int