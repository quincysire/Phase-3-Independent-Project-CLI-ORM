from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from .base import Base
#from .associations import director_movie_association
from .associations import genre_movie_association

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    genre_name = Column(String)
    movies = relationship("Movie", secondary=genre_movie_association, back_populates="genres")

    def __init__(self, genre_name):
        self.genre_name = genre_name