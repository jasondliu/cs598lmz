import weakref

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from . import config
from . import utils
from . import exceptions
from . import errors
from . import models

logger = logging.getLogger(__name__)


class Database(object):
    """
    Database connection.
    """

