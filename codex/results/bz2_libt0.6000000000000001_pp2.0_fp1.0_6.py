import bz2
bz2.open
import csv
csv.open
import datetime
datetime.date
import gzip
gzip.open
import lzma
lzma.open
import re
re.findall
import time
time.sleep
import zipfile
zipfile.ZipFile
import xml.etree.ElementTree
xml.etree.ElementTree.parse

# This does not work with Python 2.6
#from collections import Counter
#Counter.most_common

# This does not work with Python 2.6
#from collections import OrderedDict
#OrderedDict.fromkeys

from collections import defaultdict
defaultdict.default_factory
from collections import namedtuple
namedtuple.namedtuple
from collections import Counter
Counter.most_common
from collections import OrderedDict
OrderedDict.fromkeys

from itertools import chain
chain.from_iterable
from itertools import compress
compress.__next__
from itertools import count
count.__next__
from itertools import cycle
cycle.__next__
from itertools
