from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self,a: a

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from datetime import datetime, timedelta

from mongoengine.queryset.visitor import Q

from models import *
from geoloc import *

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


#GLOBAL VARIABLES
#DBN = MongoEngine()
#POLY = PolySearch()

#application = flask.Flask(__name__)
#app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
#APP.config["SECRET_KEY"] = "KeepThisS3cr3t"

#DBN.init_app(APP)

class TweetFilter():
	@classmethod
	def load_tweets(self,db,tweets_collection,state,loc_polygon):
		tweets = []
		tweet_file = open("tweet_data/"+
