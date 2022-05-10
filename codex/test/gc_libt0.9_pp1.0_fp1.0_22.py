import gc, weakref
import sys, os, re
import time, datetime, calendar
import binascii
from random import random
from collections import OrderedDict, namedtuple
from itertools import islice
from io import BytesIO, StringIO, BufferedWriter
from io import IOBase  # pytype: disable=pyi-error
from functools import partial, update_wrapper

