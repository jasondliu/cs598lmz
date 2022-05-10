import codecs
# Test codecs.register_error
import errno
# Import StringIO from cStringIO for efficiency
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import functools
import gc
import gettext
import glob
import hashlib
# hatfile should be imported before heapq
try:
    import hatfile
except ImportError:
    pass
import heapq
import imp
import inspect
import itertools
import linecache
import locale
import logging
import math
import mmap
import ntpath
import operator
import optparse
import os
import pdb
import pickle
import platform
import pprint
import profile
import pstats
import random
import re
import repr
import resource
import setpgrp
import shlex
import shutil
import signal
import simplejson
import site
import smtplib
import socket
import sre
import sre_constants
import sre_parse
import stat
import string
import struct
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import token
import tokenize
import
