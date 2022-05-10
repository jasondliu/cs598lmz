import mmap
import sqlite3
import struct
import sys
import traceback

from ctypes import sizeof, c_float
from cStringIO import StringIO

from b3.clients import Clients
from b3.config import XmlConfigParser
from b3.decorators import deprecated
from b3.functions import main_is_frozen
from b3.output import VERBOSE, DEBUG
from b3.plugins import PluginData
from b3.plugins.admin import AdminPlugin
from b3.plugins.censorurt import CensorurtPlugin
from b3.plugins.plugin import getPlugin, getConfPath
from b3.parsers.punkbuster import PunkBuster
from b3.parsers.q3a.abstractParser import AbstractParser
from b3.update import B3version

__author__ = 'ThorN'
__version__ = '1.8.1'

class Urt43Parser(AbstractParser):

    gameName = 'urt'
    OutputClass = None
    _punkbusterMessageFormats = (
        # final
        re.compile(r
