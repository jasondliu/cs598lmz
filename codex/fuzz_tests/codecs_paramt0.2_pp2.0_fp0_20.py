import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a workaround for a bug in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    codecs.lookup_error('strict')
except LookupError:
    import encodings
    encodings._cache['strict'] = encodings.search_function('utf-8')
    encodings._unknown['strict'] = encodings.search_function('utf-8')

# This is a workaround for a bug in Python 2.7.3
# See http://bugs.python.org/issue1602
try:
    import multiprocessing
except ImportError:
    pass

# This is a workaround for a bug in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    codecs.lookup_error('strict')
except LookupError:
    import encodings
    encodings._cache['strict'] = encodings.search_
