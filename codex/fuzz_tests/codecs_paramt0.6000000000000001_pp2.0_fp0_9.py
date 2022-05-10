import codecs
codecs.register_error('strict', codecs.ignore_errors)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError

from datetime import datetime
from dateutil import parser
from dateutil import tz

#from sqlalchemy.dialects.mysql import INTEGER

from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

