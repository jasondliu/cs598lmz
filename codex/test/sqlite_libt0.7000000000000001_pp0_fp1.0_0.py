import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import base64
import logging

from . import _graphite

log = logging.getLogger('graphite')

class GrafanaDataSource(object):
    def __init__(self, ds_id, ds_name):
        self.ds_id = ds_id
        self.ds_name = ds_name

class GraphiteDataSource(object):
    def __init__(self, ds_id, ds_name):
        self.ds_id = ds_id
        self.ds_name = ds_name


