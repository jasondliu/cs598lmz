import _struct
import time

from server import const
from server.const import *
from server.db import Db
from server.models import User


def get_user_by_email(email):
    user = Db.get_user_by_email(email)
    if user is None:
        return None
    return User.from_db(user)


def get_user_by_id(id):
    user = Db.get_user_by_id(id)
    if user is None:
        return None
    return User.from_db(user)


def get_user_by_session(session):
    user = Db.get_user_by_session(session)
    if user is None:
        return None
    return User.from_db(user)


def get_all_users():
    users = Db.get_all_users()
    return [User.from_db(user) for user in users]


