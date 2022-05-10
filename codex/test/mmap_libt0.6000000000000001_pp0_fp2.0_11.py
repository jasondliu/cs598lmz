import mmap
import os
import re
import socket
import struct
import sys
import time
from cStringIO import StringIO

from collections import namedtuple
from contextlib import contextmanager

from . import errors
