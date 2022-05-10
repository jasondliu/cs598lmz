import weakref

# from . import utils
from . import errors
from . import constants
from . import config
from . import utils
from . import validators
from . import requests
from .log import logger

class BaseModel(object):
    def __init__(self, **kwargs):
        self.client = kwargs.pop('client', None)
        self.bot = kwargs.pop('bot', None)
        self.session = kwargs.pop('session', None)
        self.update = kwargs.pop('update', None)

        self.id = kwargs.pop('id', None)
        self.name = kwargs.pop('name', None)
        self.username = kwargs.pop('username', None)
        self.first_name = kwargs.pop('first_name', None)
        self.last_name = kwargs.pop('last_name', None)
        self.type = kwargs.pop('type', None)
        self.all_members_are_administrators = kwargs.pop('all
