import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
import os
import re
import glob
import shutil
import urllib2
import tarfile
import zipfile
import subprocess
import datetime
import platform
import time
import ctypes
import imp
import fnmatch
import traceback
import json
import tempfile
import shutil
import uuid
import hashlib
import random
import string
import ctypes
import ctypes.util
import platform
import argparse
import subprocess
import threading
import Queue
import errno
import shutil
import time
import threading
import Queue
import errno
import socket
import struct

from distutils.version import LooseVersion

import utils
import config

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class Build(object):
    def __init__(self, arch, build_type, root_dir, build_dir, install_dir, version, is_debug_build,
        is_cross_build, is_cross_build_using_
