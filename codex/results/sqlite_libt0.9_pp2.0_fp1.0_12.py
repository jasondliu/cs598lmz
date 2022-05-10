import ctypes
import ctypes.util
import threading
import sqlite3
from xmlrpclib import Fault

from django.conf import settings

from CCORE.VFAT2CORE import VFAT2CORE
from CCORE.UDPorchard import UDPorchard
from CCORE.VFAT3CORE import VFAT3CORE
from CCORE.UDPorchard_v3 import UDPorchard3
from astropy.table import Table

from utils import HLTDB
from utils import CCDBaccess
from utils.hltlogging import hltlog
from utils.logconfig import logconfig
from utils.hltconfig import hltconfig
from utils.hltjson import OrderedUpdate
from importlib import import_module
from time import time, sleep
from copy import copy

from datetime import datetime
import time, math


from DAQ.orchardclient import get_orchard_client
from DAQ.slowcontrol_types import SlowStatusObj

log = hltlog()

def get_pybar_client():
    parameters = hltconfig('DAQ/config/pybar_client.
