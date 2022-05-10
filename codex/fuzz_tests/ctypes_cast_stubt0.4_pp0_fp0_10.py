import ctypes
ctypes.cast(ctypes.c_void_p(0), ctypes.py_object).value = None

import sys
import os
import time
import json
import shutil
import logging
import logging.handlers
import datetime
import traceback
import threading
import subprocess
import socket
import struct
import platform
import re
import ctypes
import ctypes.util
import tempfile

from . import utils
from . import consts
from . import config
from . import loghelper
from . import xlogging
from .utils import load_json_file, save_json_file, load_binary_file, save_binary_file
from .utils import get_ip_by_name, get_local_ip, get_local_ip_by_name, get_local_ip_by_mac
from .utils import get_local_mac, get_local_mac_by_name, get_local_mac_by_ip
from .utils import get_local_name, get_local_name_by_ip, get_local_name_by_mac
from .utils import get_local
