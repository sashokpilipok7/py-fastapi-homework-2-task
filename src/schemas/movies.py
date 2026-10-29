from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: str
    orig_lang: str
    budget: float
    revenue: float
    country_id: int

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass


class MovieDetailSchema(MovieBase):
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