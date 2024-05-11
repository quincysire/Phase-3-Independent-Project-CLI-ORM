import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.director import Director
from models.base import Base
from main import session


parser = argparse.ArgumentParser(description="Movie store")
parser.add_argument("-ad", "-adddr", help="Add director")
parser.add_argument("-ld", "-listdr", action="store_true", help="List all directors")
parser.add_argument("-am", "-addmv", help="Add movie")
args = parser.parse_args()

if args.ad:
    director = Director(args.ad)
    session.add(director)
    session.commit()
elif args.ld:
    directors = session.query(Director).all()
    for director in directors:
        print(director.name)
elif args.am:
    # Add movie functionality
    pass  # You need to implement this part
else:
    print("Invalid command!")