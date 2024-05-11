from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import director_movie_association

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    movies = relationship("Movie", secondary=director_movie_association, back_populates="directors")

    def __init__(self, name):
        self.name = name

    def add_movie(self, movie):
        self.movies.append(movie)