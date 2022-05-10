import codecs
# Test codecs.register_error('text', 'MyTestError', lambda e: ('{}(%s)'.format(e.__class__.__name__) % e.object[e.start:e.end]), 'Name of error')
# codecs.register_error('text', 'MyTestError', lambda e: ('{}(%s)'.format(e.__class__.__name__) % e.object[e.start:e.end]), 'Name of error')
try:
    import html
except ImportError:
    import HTMLParser as html


# PY2
