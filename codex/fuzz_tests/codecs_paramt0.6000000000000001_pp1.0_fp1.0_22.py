import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 3 compatibility
try:
    from urllib.parse import unquote
except ImportError:
    from urllib import unquote

# Find the best implementation available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

# Find a JSON parser
try:
    import simplejson as json
    assert hasattr(json, 'loads') and hasattr(json, 'dumps')
except ImportError:
    try:
        from django.utils import simplejson as json
        assert hasattr(json, 'loads') and hasattr(json, 'dumps')
    except ImportError:
        import json
        assert hasattr(json, 'loads') and hasattr(json, 'dumps')

# A true, case-sensitive dictionary
try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

# A set type
try:
    set
except NameError:
    from sets import Set as set

# Bytes literals
