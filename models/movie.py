from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from .base import Base
from .associations import director_movie_association
from .associations import genre_movie_association
from .associations import viewer_movie_association

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    directors = relationship("Director", secondary=director_movie_association, back_populates="movies")
    genres = relationship("Genre", secondary=genre_movie_association, back_populates="movies")
    viewers = relationship("Viewer", secondary=viewer_movie_association, back_populates="movies")

    def __init__(self, title, director, genre):
        self.title = title
        self.directors.append(director)
        self.genre = genre
        self.genres.append(genre)
        