import mmap
import os
import shutil
import sys
import tempfile
import time
import unittest

from contextlib import contextmanager
from distutils.version import LooseVersion
from functools import partial
from os import path
from subprocess import Popen, PIPE

from mock import patch

