import _struct
import _thread
import _time

_VER = sys.version_info

# Begin Python 2/3 compatibility

if _VER[0] >= 3:
    string_types = str,
    XXX_b = lambda m: m.encode()
    XXX_u = lambda m: m
    import _io
    XXX_FileType = _io.FileIO or _io.BytesIO
else:
    string_types = basestring,
    XXX_b = lambda m: m
    XXX_u = lambda m: unicode(m, 'unicode_escape')
    import StringIO
    XXX_FileType = StringIO.StringIO

# End Python 2/3 compatibility


class simple_message(object):
    '''
    A simple message type.
    '''

    def __init__(self, message, category, filename, lineno, line=None):
        '''
        Create a message.
        '''
        self.message = message
        self.category = category
        self.filename = filename
        self.lineno = lineno
        self
