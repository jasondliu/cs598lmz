import mmap
import os
import re
import sys
import time

from collections import defaultdict
from collections import namedtuple
from contextlib import closing
from datetime import datetime
from itertools import chain
from itertools import groupby
from itertools import imap
from itertools import islice
from itertools import izip
from itertools import tee
from operator import attrgetter
from operator import itemgetter
from operator import methodcaller
from optparse import OptionParser
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from tempfile import NamedTemporaryFile
from tempfile import mkdtemp
from tempfile import mkstemp
from tempfile import mkstemp_compat
from tempfile import TemporaryFile
from threading import Lock
from threading import Thread
from time import sleep
from traceback import format_exc
from weakref import WeakKeyDictionary

from mercurial import (
    cmdutil,
    commands,
    context,
    dirstate,
    error,
    extensions,
    hg,
