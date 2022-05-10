import codecs
codecs.register_error('xmlcharrefreplace', lambda e: (u'', e.start + 1))

from rdflib.py3compat import PY3, is_literal
import logging
if PY3:
    from io import StringIO
else:
    from StringIO import StringIO

_logger = logging.getLogger(__name__)

def escape(s):
    # to XML name
    return s.replace(' ', '_')

def unescape(s):
    # from XML name
    return s.replace('_', ' ')

def _quote(s):
    if '"' in s:
        if "'" in s:
            s = '"%s"' % s.replace('"', "&quot;")
        else:
            s = "'%s'" % s
    else:
        s = '"%s"' % s

    return s

def _quote_smart(s):
    """
    Quote a string if either:
    a) it is not a valid XML name
    b) it's a number
    """

