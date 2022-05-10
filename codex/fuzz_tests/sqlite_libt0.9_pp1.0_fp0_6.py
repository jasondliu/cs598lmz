import ctypes
import ctypes.util
import threading
import sqlite3
import random
import os
import sys
import time
import uuid
import shutil
import json
import math
import base64

from threading import Event, Thread, Lock
from pprint import pprint
from operator import add
from datetime import datetime
from html.parser import HTMLParser

from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, ExecutionProfile, NoHostAvailable, UnsupportedOperation
from cassandra.query import SimpleStatement, BatchStatement, dict_factory
from cassandra.query import tuple_factory, named_tuple_factory
from cassandra.util import uuid_from_time
from datastax.io.libevreactor.LibevConnection import LibevConnection

from ctypes import *

def _offt_to_long(offset):
    if ctypes.sizeof(c_void_p) == 4:
        return c_long.from_address(offset).value
    else:
        return c_longlong.from_address(offset).value

def _long
