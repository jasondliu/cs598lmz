import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import islice, chain
from operator import itemgetter
from threading import Lock

from six import iteritems, itervalues
from six.moves import xrange

