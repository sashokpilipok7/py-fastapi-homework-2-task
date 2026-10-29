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
    country: Optional[str] = None
    genres: list[str] = []
    actors: list[str] = []
    languages: list[str] = []

class MovieCreate(MovieBase):
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]

class MovieUpdate(MovieBase):
    name: Optional[str] = None
    date: Optional[date] = None
    score: Optional[float] = None
    overview: Optional[str] = None
    status: Optional[MovieStatusEnum] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None


class MovieListItemSchema(MovieBase):
    id: int
    name: str
    date: date
    score: float
    overview: str
    model_config = ConfigDict(from_attributes=True)

class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int