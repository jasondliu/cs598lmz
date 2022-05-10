import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask

from config import configure_app
from celery import Celery


from models.domain import User, Patron
from models.domain import db as _db


from settings import config
from settings.codec import CODEC

#Initialize the web app
app = Flask(__name__)
configure_app(app)

#Initialize the database and register the models
db.init_app(app)
with app.app_context():
     db.create_all()

cel = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])

initial_plays = {
    'week':         config.Config.PLAY_LIMITS['WEEK'],
    'day':          config.Config.PLAY_LIMITS['DAY'],
    'consecutive':  config.Config.PLAY_LIMITS['CON
