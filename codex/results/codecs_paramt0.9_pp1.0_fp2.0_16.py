import codecs
codecs.register_error('strict', codecs.strict_errors)

import struct, time, os

from collections import OrderedDict

# Shortcuts
find = None
find_all = None
find_one = None

def _find_one(selector):
    res = find_all(selector)
    if len(res):
        return res[0]
    return None

def _find_wrapper(f, selector):
    return f(selector, _tag_re)

def _unquote(str):
    if str == None or len(str) == 0:
        return str
    # remove quotation marks around str
    if str[0] == '"' and str[-1] == '"':
        str = str[1:-1]
    return str

def _get_start_end(self):
    # returns a 2-tuple: (start_byte, end_byte)
    if self.sig_flags[0] in ('m', 'M'):
        # multiple-block signature
        end = self.sig_flags[1]

