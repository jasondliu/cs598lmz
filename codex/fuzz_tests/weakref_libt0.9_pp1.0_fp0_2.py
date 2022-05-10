import weakref

from rq import TimeoutExpired
import requests

from . import login_manager
from . import redis_conn, redis_conn_kv
from .config import Config, CACHE_USER_FOR because_cache


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id, username, password_hash, realname, wx_open_id, wx_app_id, wx_session_key, wx_access_token, wx_refresh_token = (
        db.Column(db.Integer, primary_key=True, index=True),
        db.Column(db.String(20), nullable=False, unique=True),
        db.Column(db.String(100), nullable=False),
        db.Column(db.String(20)),
        db.Column(db.String(50), index=True),
        db.Column(db.String(20)),
        db.Column(db.String(200)),
        db.Column(db.String(500)),
        db.Column
