import threading
threading.Thread(target=lambda: None).start()

import time
time.sleep(1)

import os
os.path.exists("/")

import sys
sys.version_info

import re
re.compile("")

import json
json.dumps([])

import math
math.pi

import cmath
cmath.pi

import decimal
decimal.Decimal(1)

import fractions
fractions.Fraction(1, 2)

import random
random.random()

import urllib
urllib.urlopen("http://www.python.org")

import hashlib
hashlib.md5("").hexdigest()

import hmac
hmac.HMAC("", "").hexdigest()

import itertools
list(itertools.islice(itertools.count(), 10))

import collections
collections.Counter("abc")

import bisect
bisect.bisect_left([1, 2, 3], 2)

import array
