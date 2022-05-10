import lzma
lzma.LZMA_AVAILABLE = False

import os
import sys
import time
import json
import base64
import struct
import socket
import traceback
import threading
import subprocess
import collections
import contextlib
import itertools
import multiprocessing

import pytest

import zmq
from zmq import Context, ZMQError, ZMQBindError
from zmq.utils import jsonapi
from zmq.utils.strtypes import b, u, bytes, unicode
from zmq.tests import BaseZMQTestCase, SkipTest, have_gevent, GreenTest, \
    skip_pypy
from zmq.utils.strtypes import asbytes, asstr, b, u, bytes, unicode, basestring
from zmq.utils.win32 import allow_interrupt

if have_gevent:
    import gevent
    import gevent.monkey
    gevent.monkey.patch_all()

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------

if sys.version_info[0] >= 3
