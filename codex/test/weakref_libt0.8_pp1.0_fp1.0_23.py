import weakref
from threading import RLock

from celery import current_app as celery_app
from kombu import Exchange, Queue
from flask import current_app
from flask_login import UserMixin

from . import db, bcrypt, cache, login_manager
from . import sendgrid
from .utils import send_email


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Role %r>" % self.name

    def __str__(self):
        return self.name


