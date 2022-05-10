import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from flask import Flask, request, render_template, redirect, abort, jsonify, Response
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func, Table, Column, Integer, ForeignKey, Unicode, DateTime, Float
from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import cast
from sqlalchemy.dialects.mysql import LONGTEXT
from flask.ext.cache import Cache
from datetime import datetime
import json
import hashlib
from flask.ext.compress import Compress
from celery import Celery
from celery.utils.log import get_task_logger
from rdflib import Graph, ConjunctiveGraph
from rdflib.compare import graph_diff
from rdflib.plugins
