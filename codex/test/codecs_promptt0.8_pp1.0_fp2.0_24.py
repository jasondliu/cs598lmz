import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

import json
import sys

def __get_data():
    raise ImportError('Failed to import module')

data = dict()
try:
    data = __get_data()
except ImportError:
    pass

