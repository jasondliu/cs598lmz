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


class DB(object):

    # TODO: make the DB name configurable
    DB_NAME = 'grafana.db'
    SQL_INIT = '''
        CREATE TABLE IF NOT EXISTS data_sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS dashboards (
            id INTEGER PRIMARY KEY AUTOINCREMENT
