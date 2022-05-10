import mmap
import os
import shutil
import subprocess
import sys
import time
import traceback
import uuid

from collections import namedtuple
from collections import OrderedDict
from functools import partial
from itertools import chain
from itertools import product
from operator import attrgetter
from operator import itemgetter
from operator import methodcaller
from operator import mul
from operator import truediv
from random import randint
from random import shuffle
from subprocess import CalledProcessError
from tarfile import TarFile
from tarfile import TarInfo
from tempfile import mkdtemp
from tempfile import mkstemp
from tempfile import NamedTemporaryFile
from threading import Event
from threading import Thread
from threading import Timer

from six import iteritems
from six import itervalues
from six.moves import range
from six.moves import urllib

from ansible import constants as C
from ansible.compat.six import string_types
from ansible.compat.six.moves import input
from ansible.compat.six.moves import
