import _struct
import zlib

from ._compat import FileExistsError, PermissionError, PY2, PY3, \
    URLError, urljoin
from .exceptions import ConnectionError, InvalidArchiveError, \
    InvalidChecksumError, InvalidChecksumFormatError, \
    MaxRedirectsExceededError, NoChecksumError, \
    NoRedirectsAllowedError, RetrievalError, UnsupportedArchiveFormatError, \
    UnsupportedChecksumFormatError, VerificationError
from .util import default_py_version, execute_command, get_file_mode, \
    is_archive, is_string, makedirs, remove_file, url_to_path, url_to_path_unquote


logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 60.0

if PY3:
    from urllib.parse import urlparse, urlunparse
else:
    from urlparse import urlparse, urlunparse


