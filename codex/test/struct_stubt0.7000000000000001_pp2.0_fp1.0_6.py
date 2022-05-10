from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack = Struct.pack
s.unpack = Struct.unpack
s.unpack_from = Struct.unpack_from

import array
from array import array
array = array.array

#from array import *

from collections import deque
from collections import defaultdict

from itertools import chain
from itertools import tee
from itertools import imap
from itertools import izip
from itertools import repeat
from itertools import dropwhile
from itertools import takewhile
from itertools import islice
from itertools import izip_longest
from itertools import count
from itertools import starmap
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import groupby

from ordereddict import OrderedDict
from threading import Lock
from threading import Thread
from threading import current_thread
from threading import local

