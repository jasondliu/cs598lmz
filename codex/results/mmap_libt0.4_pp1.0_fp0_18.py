import mmap
import os
import re
import sys
import tempfile
import time
import traceback

from collections import defaultdict
from datetime import datetime
from itertools import chain, count
from optparse import OptionParser

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

from pymongo.son_manipulator import AutoReference, NamespaceInjector

from bson.code import Code
from bson.son import SON

from bson.objectid import ObjectId
from bson.dbref import DBRef

from pymongo.errors import (AutoReconnect,
                            ConfigurationError,
                            InvalidName,
                            OperationFailure)

from pymongo.read_preferences import ReadPreference

from pymongo.uri_parser import parse_uri

from pymongo.mongo_client import MongoClient
from pymongo.database import Database

from pymongo.collection import Collection

from pymongo.cursor import Cursor

from pymongo.errors import (ConnectionFailure,

