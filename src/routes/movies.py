from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database import get_db, MovieModel
from database.models import CountryModel, GenreModel, ActorModel, LanguageModel
from schemas.movies import MovieListResponseSchema

router = APIRouter()

@router.get("/movies", response_model=MovieListResponseSchema)
async def get_movies(db: AsyncSession = Depends(get_db())):
    movies = []
    return movies
