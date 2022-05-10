import ctypes
import ctypes.util
import threading
import sqlite3


class HostFile(object):
    def __init__(self, host, path):
        self.host = host
        self.path = path

    def __repr__(self):
        return 'HostFile(host=%r, path=%r)' % (self.host, self.path)


class Host(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'Host(id=%r, name=%r)' % (self.id, self.name)


class HostFileDatabase(object):
    class _HostFileDatabaseConnection(object):
        def __init__(self, cursor):
            self.cursor = cursor

        def _fetch(self, query, args=()):
            self.cursor.execute(query, args)
            return self.cursor.fetchall()

        def _fetchone(self, query, args=()):
            return self._fetch(query, args)[0]

        def _
