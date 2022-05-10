import codecs
codecs.register_error('ignore_replacement', codecs.lookup('ignore'))

from math import pow
from sys import argv
from os import mkdir, path
from random import seed, randint, randrange
from itertools import cycle, chain
from datetime import datetime, timedelta
from json import dumps, loads
from collections import OrderedDict
from time import time, sleep
from multiprocessing import Process, Queue, cpu_count

#from crypto.compat import argv, mkdir, path, seed, randint, randrange, cycle, chain, datetime, timedelta, dumps, loads, exit, time, sleep, Process, Queue, cpu_count

try:
    from  collections import OrderedDict
except:
    from ordereddict import OrderedDict

from crypto.utility import parse_date, parse_delta, get_files, get_files_from_list, get_lines
from crypto.configuration.children import Accounts
from crypto.configuration.database import quotes_coll 
import crypto.bitfinex.download_quotes as b_d_q

