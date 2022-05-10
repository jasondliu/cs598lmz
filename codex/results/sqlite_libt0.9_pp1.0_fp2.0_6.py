import ctypes
import ctypes.util
import threading
import sqlite3
import pickle
import os
import inspect
import sys
import importlib
import re
import traceback
import copy
import networkx
import json
import logging

#### For hashing immutable types
import hashlib
import datetime

#### For sorting objects
import operator

# Initialize logging
logging.basicConfig(
        format='%(asctime)s %(levelname)s %(name)s: %(message)s', 
        level=logging.ERROR,
        stream=sys.stderr,
    )

pgwrap_key = 0
pgwrap_dict = {}

#### pybind11 only allows one extension class per module, so we need to put
#### the types in separately modules
#### https://github.com/pybind/pybind11/issues/922
pg_partition_objects_module = importlib.import_module('pg_partition_objects')

#### Types we're going to rebind as part of the interface
#### pg_partition_object(LibPyGridtools,Partition,PyObject)

#### pg_partition_rectil
