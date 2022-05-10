import gc, weakref
from ..lib.utils import get_random_string
from ..lib.logger import debug
from ..lib.auth import AuthUser
from ..lib.db import get_dbm
from ..lib.decorators import classproperty

import pytest
import asyncio

class Base:
    def __init__(self, name):
        self.name = name

    @classproperty
    def logger(cls):
        return logging.getLogger(cls.__name__)


class User(AuthUser, Base):
    def __init__(self, name, email, password):
        super().__init__(name)
        self.email = email
        self.password = password


class Session:
    def __init__(self, user, app):
        self.user = user
        self.app = app

    def __enter__(self):
        self.old_user = self.app.current_user
        self.app.current_user = self.user
        return self.user

    def __exit__(self, *args):
        self.app.
