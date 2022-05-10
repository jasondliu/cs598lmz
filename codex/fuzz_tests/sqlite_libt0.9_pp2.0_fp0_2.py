import ctypes
import ctypes.util
import threading
import sqlite3

from contextlib import contextmanager

from pymongo import MongoClient, ReadPreference, ASCENDING
from pymongo.errors import NetworkTimeout
from gridfs.errors import CorruptGridFile, NoFile

from remotecv import models, utils
from remotecv.utils import ssh
from remotecv.exceptions import InvalidVideoFile
from remotecv.models.directory_observable import DirectoryObservable
from remotecv.models.video_frame_generator import VideoFrameGenerator


class DbModelMixin(object):
    def save(self):
        try:
            self.to_db()
        except sqlite3.OperationalError:
            self.recreate_db()
            self.to_db()


class Directory(models.Directory, DbModelMixin):
    pass


class DirectoryWatcher(Directory):
    def __init__(self, name, local_path='/opt/remotecv/media/'):
        super(DirectoryWatcher, self).__init__(name, local_path)
