import gc, weakref
from time import time
from os import remove
from os.path import exists, join, dirname, normpath
from itertools import chain
from threading import Event
from hashlib import md5
