import mmap
import re
import gzip
import sys
from io import StringIO
from io import BytesIO
from collections import deque
from itertools import islice
from contextlib import closing
from fuzzywuzzy.fuzz import ratio
from fuzzywuzzy.process import extract
from fuzzywuzzy.process import extractBests
from fuzzywuzzy.process import extractOne

def p(obj):
  return pickle.dumps(obj)

def unp(str):
  return pickle.loads(str)

def ungzip(str):
  buffer = BytesIO(str)
  return gzip.GzipFile(fileobj=buffer)
