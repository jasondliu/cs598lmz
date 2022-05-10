import gc, weakref, traceback
from collections import defaultdict
from functools import partial
from itertools import count
import io, pdb, sys, operator


__all__ = [
    'take', 'retake', 'chain', 'tee', 'grouper', 'partition',
    'iteritems', 'iterkeys', 'itervalues', 'iterlists',
    'first', 'rest', 'last', 'takewhile', 'dropwhile', 'tail',
    'chunks', 'partition_all', 'consume',
    'unique_everseen', 'unique_justseen',
    'always_iterable', 'always_reiterable',
    'sided', 'slice', 'sliding_window',
    'window', 'roundrobin', 'powerset',
    'restart_on', 'merge_sorted',
    'fibonacci', 'lazythis',
    'peekable',
    'one', 'ilen',
    'all_equal'
    ]


def always_iterable(x):
    """
Adapt an iterable so that
