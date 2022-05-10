import ctypes
import ctypes.util
import threading
import sqlite3

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def sqlite_escape(s):
    return s.replace("'","''")

class ServerData:
    def __init__(self, data):
        self.name = str(data['name'])
        self.map = str(data['map'])
        self.gameMode = str(data['gameMode'])
        self.gameType = str(data['gameType'])
        self.password = data['password']
        self.featuredMod = data['featuredMod'].split("\
