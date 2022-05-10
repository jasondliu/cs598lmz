import weakref
# Test weakref.ref
try:
    weakref.ref
except AttributeError:
    from weakref_backport import ref

import hmac


def secure_filename(filename):
    """Secure filename from an insecure/invalid filename.

    Note: This is a best-effort, since it's not always possible to determine
    the true extension!

    :param filename: an insecure filename
    """
    for sep in os.path.sep, os.path.altsep:
        if sep is not None:
            filename = filename.replace(sep, " ")
    return "".join(x for x in filename if x.isalnum() or x in _FILENAME_VALID_CHARS)


_FILENAME_VALID_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)

_DEFAULT_CHECK_MD5 = False
_DEFAULT_MAX_FILE_SIZE = 2 ** 20  # 1 MB


class UploadedFile(object):
    """Represents an uploaded file."""

    def __init__
