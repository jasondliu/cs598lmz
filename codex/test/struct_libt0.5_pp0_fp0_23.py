import _struct
import time
import datetime
import binascii
import sqlite3
import uuid
import traceback
import logging
import os

from . import db
from . import settings
from . import exceptions
from . import utils
from . import model
from . import constants
from . import errors
from . import _struct
from . import _compat

logger = logging.getLogger(__name__)

class Base(object):
    """
    Base class for all object types.
    """
    def __init__(self, connection=None, **kwargs):
        self.connection = connection

    def to_dict(self):
        """
        Return a dict representation of the object.
        """
        raise NotImplementedError

    def to_json(self):
        """
        Return a json representation of the object.
        """
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.to_json()

