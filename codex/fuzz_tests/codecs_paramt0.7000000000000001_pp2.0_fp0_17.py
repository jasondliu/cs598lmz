import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    import cPickle as pickle
except ImportError:
    import pickle

import os
import sys

# Python 3.2 compatibility -- Python 3.2's json.load and json.loads functions
# don't have the 'encoding' parameter.
#
# This function adds the parameter to the Python 3.2 json.loads function.
#
# This function is only used in Python 3.2.
#
# Json.load and json.loads are used to read and write pickled data files.
def _loads_3_2(s, encoding=None, cls=None, object_hook=None, parse_float=None,
               parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return json.loads(s, object_hook=object_hook, parse_float=parse_float,
                      parse_int=parse_int, parse_constant=parse_constant,
                      object_pairs_hook=object_pairs_hook, **kw)
