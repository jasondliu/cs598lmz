import lzma
lzma.open(fp, mode='rb')

# urllib3/util/url.py
from .request import RequestMethods
...
from .response import is_fp_closed

if not isinstance(filename, (str, bytes, os.PathLike)):
    raise TypeError("Invalid filename: %r" % filename)

# urllib3/response.py
def is_fp_closed(fp):
    try:
        fp.tell()
        return False
    except ValueError:
        # See https://github.com/shazow/urllib3/issues/863
        return True
    except Exception:
        # Any other exception means the fp is in an unusable state.
        if isinstance(fp, _FAKE_STREAM):
            # See https://github.com/shazow/urllib3/issues/1339
            # This exception is ultimately caused by iterator exhaustion
            # from when `ImageFile.Parser` attempts to read from the stream.
            # The best we can do to detect this is a non-IOError, so this
