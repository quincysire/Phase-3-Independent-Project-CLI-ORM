from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base
director_movie_association = Table(
    'director_movie_association',
    Base.metadata,
    Column('director_id', Integer, ForeignKey('directors.id')),
    Column('movie_id', Integer, ForeignKey('movies.id')), 
)

genre_movie_association = Table(
    'genre_movie_association',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre', Integer, ForeignKey('genres.id'))
)

viewer_movie_association = Table(
    'viewer_movie_association',
    Base.metadata,
    Column('viewer_id', Integer, ForeignKey('viewers.id')),
    Column('movie_id', Integer, ForeignKey('movies.id'))
)