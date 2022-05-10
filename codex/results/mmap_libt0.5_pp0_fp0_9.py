import mmap
import random
import sys
import time

from datetime import datetime
from pprint import pprint

from bson import json_util
from bson.binary import Binary
from bson.objectid import ObjectId
from bson.son import SON

from mongo_connector import errors
from mongo_connector.constants import (DEFAULT_BATCH_SIZE, DEFAULT_MAX_BULK,
                                       DEFAULT_MAX_BATCH_DURATION)
from mongo_connector.util import retry_until_ok
from mongo_connector.doc_managers.doc_manager_simulator import DocManager
from pymongo import ReadPreference
from pymongo.errors import AutoReconnect, OperationFailure

"""
This is the DocManager class for handling documents from MongoDB
collections.
"""


LOG = logging.getLogger(__name__)


class DocManagerMongoDB(DocManager):
    """The DocManager class creates a connection to the backend engine and
        adds/removes documents, and in the case of rollback,
