import codecs
codecs.register_error('strict', codecs.ignore_errors)

# this is a hack to get around the fact that we can't
# use unicode_literals in Python 2.6
def u(s):
    if sys.version_info[0] >= 3:
        return s
    else:
        return codecs.unicode_escape_decode(s)[0]

# this is a hack to get around the fact that we can't
# use unicode_literals in Python 2.6
def b(s):
    if sys.version_info[0] >= 3:
        return s.encode('utf-8')
    else:
        return s

# this is a hack to get around the fact that we can't
# use unicode_literals in Python 2.6
def b2u(s):
    if sys.version_info[0] >= 3:
        return s.decode('utf-8')
    else:
        return s

def get_file_contents(filename):
    with open(filename, 'rb') as f:
        return f.
