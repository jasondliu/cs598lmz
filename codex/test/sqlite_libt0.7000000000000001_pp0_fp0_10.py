import ctypes
import ctypes.util
import threading
import sqlite3
import sys
from ctypes.util import find_library

from .. import base
from .. import config


class Tag(base.DBObject):
    tablebase = 'tags'
    defaults = dict(base.DBObject.defaults, tag='', weight=1, name='',
                    count=0)

    def __init__(self, id, conn=None, cursor=None):
        if conn is None:
            conn = sqlite3.connect(config.get('database', 'path'))
        base.DBObject.__init__(self, id, conn, cursor)

    def _update(self, d):
        base.DBObject._update(self, d)
        if 'tag' in d:
            self.tag = d['tag']
        if 'weight' in d:
            self.weight = d['weight']
        if 'name' in d:
            self.name = d['name']
        if 'count' in d:
            self.count = d['count']

