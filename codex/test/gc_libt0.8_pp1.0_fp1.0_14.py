import gc, weakref

from os import makedirs, environ, remove
from os.path import basename, dirname, join, isfile
from shutil import rmtree
from time import time

from distutils.version import LooseVersion

