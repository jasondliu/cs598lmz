import gc, weakref
from time import time
from collections import deque, defaultdict

from .. import utils, config, signals, __version__
from ..utils.log import get_logger
from ..utils.misc import (
    format_time,
    format_size,
    format_number,
    format_speed,
    get_filesystem_encoding,
    get_filesystem_errors,
    sanitize_open,
)
from ..utils.encoding import (
    preferredencoding,
    fs_decode,
    fs_encode,
    fs_is_case_insensitive,
)
from ..utils.compat import (
    PY2,
    text_type,
    urlparse,
    urlunparse,
    urlencode,
    urljoin,
    urlopen,
    unquote,
    quote,
    urlretrieve,
    Cookie,
    HTTPCookieProcessor,
    HTTPError,
    Request,
    build_opener,
    install_opener,
    urlsplit,
    parse_qs,
