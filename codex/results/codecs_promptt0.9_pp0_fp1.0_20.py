import codecs
# Test codecs.register_error('text', 'MyTestError', lambda e: ('{}(%s)'.format(e.__class__.__name__) % e.object[e.start:e.end]), 'Name of error')
# codecs.register_error('text', 'MyTestError', lambda e: ('{}(%s)'.format(e.__class__.__name__) % e.object[e.start:e.end]), 'Name of error')
try:
    import html
except ImportError:
    import HTMLParser as html


# PY2
if sys.version_info < (3,):
    text_type = unicode
    binary_type = str
    string_types = (str, unicode)
    class_types = (type, types.ClassType)
else:
    text_type = str
    binary_type = bytes
    string_types = (str,)
    class_types = (type,)

import numpy as np
_NP_UNICODE_TYPE = np.unicode_
if _NP_UNICODE_TYPE is bytes and sys
