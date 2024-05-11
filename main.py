from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.movie import Movie
from models.director import Director
from models.base import Base
from models.genre import Genre
from models.viewer import Viewer

DATABASE_URL = "sqlite:///movielist.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def main():

    director1 = Director("Quincy")
    director2 = Director("Segem")
    genre1 = Genre("Fiction")
    genre2 = Genre("Crime")
    movie1 = Movie("Mr.Robot", director1, genre1)
    movie2 = Movie("Wisdom of crowd", director2, genre2)
    movie3 = Movie("The Hack", director1, genre1)
    movie4 = Movie("Swordfish", director1, genre2)
    movie5 = Movie("Algorithm", director2, genre1)

    viewer1 = Viewer('Sandra')
    viewer2 = Viewer('Jane')
    viewer1.watch_movie(movie1)
    viewer1.watch_movie(movie4)
    viewer2.watch_movie(movie3)
    viewer1.watched_movies()
    print("running")

    session.add(director1)
    session.add(director2)
    session.add(movie1)
    session.add(movie2)
    session.add(viewer1)
    session.add(viewer2)

    session.commit()

if __name__ == "__main__":
    main()