import codecs
codecs.register_error('surrogate_or_special', codecs.surrogatepass)

# Some other bits from six
import sys
if sys.version_info[0] < 3:
    import itertools
    zip = itertools.izip
    range = xrange

    # Create a bytes version of str type
    import types
    class bytes(str):
        def join(self, iterable):
            return b"".join(iterable)
    bytes.__name__ = b"bytes"
    bytes.__module__ = types.__name__
else:
    import io
    StringIO = io.StringIO
    BytesIO = io.BytesIO
    zip = zip
    range = range

    # Create a str version of bytes type
    import types
    class str(bytes):
        def join(self, iterable):
            return "".join(iterable)
    str.__name__ = "str"
    str.__module__ = types.__name__


def update_add(dest, new):
    """Updates a dictionary with keys and values from 'new
