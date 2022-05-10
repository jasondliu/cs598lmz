import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# import pymysql
import pymysql

# import sqlalchemy_utils
import sqlalchemy_utils

# import logging
import logging

# instantiate SQLAlchemy
db = SQLAlchemy()

# instantiate logger
logger = logging.getLogger(__name__)

# define database for app
def database(app):

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{pw}@{host}/{db}'.format(user="root",pw="",host="localhost",db="test")
    # app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_POOL_RECYCLE']
