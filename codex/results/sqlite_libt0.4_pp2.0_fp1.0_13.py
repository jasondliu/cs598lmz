import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import getopt
import subprocess
import re
import signal
import socket
import struct

from collections import defaultdict

from ctypes import *
from ctypes.wintypes import *

from db import *
from net import *
from util import *

# https://msdn.microsoft.com/en-us/library/windows/desktop/aa365783(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa365788(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa366045(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa366050(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa366058(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop
