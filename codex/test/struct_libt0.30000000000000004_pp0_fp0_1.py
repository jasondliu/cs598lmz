import _struct
import _struct_ext
import _struct_ext_ext

from _struct_ext import *
from _struct_ext_ext import *

from _struct import *

from _struct import __doc__

__all__ = _struct_ext.__all__ + _struct_ext_ext.__all__

#
# The following is a hack to make the docstrings for the struct module
# appear in the Python documentation.
#

import sys
import types

def _add_doc(name, doc):
    if sys.version_info[0] < 3:
        name = name.encode('latin-1')
    if type(doc) == types.StringType:
        if sys.version_info[0] < 3:
            doc = doc.encode('latin-1')
        doc = doc.replace('\n', '\n    ')
        doc = '    ' + doc
    else:
        doc = ''
