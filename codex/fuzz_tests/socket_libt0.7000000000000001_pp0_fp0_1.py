import socket
import struct
import json
from collections import namedtuple
from utils import *
from snapshot import Snapshot
from config import Config
from logger import *

class File(object):
    def __init__(self, fd, path, size, flag, mode, version):
        self.fd = fd
        self.path = path
        self.size = size
        self.flag = flag
        self.mode = mode
        self.version = version

class FileManager(object):
    def __init__(self, app):
        self.app = app
        self.files = {}
        self.version = 0
        self.deleted = []

    def open(self, path, flag, mode):
        self.version += 1
        fd = self.app.client.create(path, 1, -1)
        if fd < 0:
            if fd == -errno.EEXIST:
                if flag & os.O_CREAT and flag & os.O_EXCL:
                    return -errno.EEXIST
                else:
                    f
