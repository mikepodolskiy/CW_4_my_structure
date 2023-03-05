# import required classes
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.dao.favorite import FavoriteDAO
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService
from app.service.user import UserService
from app.service.favorite import FavoriteService
from app.setup_db import db

# creating Dao objects, with session
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

# creating Service objects with dao object
director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
favorite_service = FavoriteService(dao=favorite_dao)
