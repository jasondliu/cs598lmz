import gc, weakref, sys

from . import instance
from . import bucket
from . import cache
from . import core
from . import ds_field
from . import graph_index
from . import inode
from . import txn
from . import txn_manager
from . import utils

from .bucket import Bucket
from .cache import ObjectCache
from .db import DB
from .graph_index import FieldIndex, CompositeIndex
from .structures import DecisionSet, MultiMap, PriorityQueue
from .txn import Transaction

from .metadb import MetaDatabase
from .object_validator import ObjectValidator

from . import sqlite_toposort


class MigratorSchemaMismatch(Exception):
    pass


class MigratorState(Enum):
    SINGLE_DS_DB = 'SINGLE_DS_DB'
    MULTI_DS_DB = 'MULTI_DS_DB'
    FINAL_DB = 'FINAL_DB'


class Migrator(object):
    _STATE_TRANSITIONS = {MigratorState.SING
