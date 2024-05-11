from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from .base import Base
from .associations import viewer_movie_association

class Viewer(Base):
    __tablename__ = 'viewers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    movies = relationship("Movie", secondary=viewer_movie_association, back_populates="viewers")


    def __init__(self, name):
        self.name = name

    def watch_movie(self, movieName):
        self.movies.append(movieName)

    def watched_movies(self):
        for movie in self.movies:
            print(movie.title)
    