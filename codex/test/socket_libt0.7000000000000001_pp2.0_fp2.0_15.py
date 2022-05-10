import socket
from time import sleep
import sys
import time

from threading import Thread
import threading
import Queue

from nose.plugins.skip import SkipTest

from Database import DB
from Utils import AsyncStreamReader, AsyncStreamWriter
from Utils import Startup, Cleanup
from Utils import GetPidByName, GetPidByName2
from SSH import SSH

from Utils import LogFile
from Utils import StatusBar
from Utils import GetIP

from Utils import GetExtraParameters


class TestBase( object ):
    '''
    A base class for all tests. It's not a test case. It mainly
    defines stuff which is common for all tests.
    '''
    def __init__( self, name ):
        '''
        Constructor
        '''
        self.logfile = None
        self.name = name
        self.db = DB()
        self.status_bar = StatusBar()
        self.ip = GetIP()
        self.ssh = SSH( self )
        self.threads = []
        self.last_pid
