import ctypes
import ctypes.util
import threading
import sqlite3
import sys
from enum import Enum, IntEnum
from ctypes import *
import Email
from Email import *

class Config(object):
    """
    Class of configuration options
    """
    def __init__(self):
        defaultConfig = self.readConfigFile("config/config.conf")
        self.address = defaultConfig.address
        self.port = defaultConfig.port
        self.user = defaultConfig.user
        self.pwd = defaultConfig.pwd
        self.smtp_server = defaultConfig.smtp_server
        self.smtp_port = defaultConfig.smtp_port
        self.domain = defaultConfig.domain
        self.uid = defaultConfig.uid
        self.gid = defaultConfig.gid
        self.DBFile = defaultConfig.DBFile
        self.listen_to_port = defaultConfig.listen_to_port
        self.sharedDir = defaultConfig.sharedDir


    def readConfigFile(self,fileName):
        """
        Reads the configuration file and returns a Config object
        """

       
