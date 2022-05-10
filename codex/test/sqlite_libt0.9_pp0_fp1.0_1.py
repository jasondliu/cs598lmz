import ctypes
import ctypes.util
import threading
import sqlite3
import collections
import logging
import os
import re
import rsa
from misc import ErrorHandler
from errcode import errstr
import net
from crypto import crypto_
from crypto import crypto
from misc import Misc
import global_
import upnp


class Sbhc:
    """ Singleton class
    """
    inst = None

    @staticmethod
    def set_inst(ninst):
        if Sbhc.inst and ninst:
            raise RuntimeError('Singleton already created')
        Sbhc.inst = ninst

    def __init__(self):
        self.netif = None
        self.log = Log()
        self.eh = ErrorHandler(self.log)
        self.edb = EventDB()
        self.udb = UserDB()
        self.cdb = ContactsDB()
        self.gdb = GroupDB()
