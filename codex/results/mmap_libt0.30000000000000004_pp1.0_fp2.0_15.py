import mmap
import os
import re
import sys

from . import _util
from . import _compat
from . import _config
from . import _errors
from . import _file
from . import _metadata
from . import _text
from . import _vcs
from . import _version
from . import _winreg

from . import _vendor
from . import _vendor.six import text_type

from . import _vendor.six.moves import input

from . import _vendor.six.moves.urllib.parse import urlparse

from . import _vendor.six.moves.urllib.request import (
    urlopen,
    Request,
    url2pathname,
    pathname2url,
)

from . import _vendor.six.moves.urllib.error import HTTPError

from . import _vendor.six.moves.urllib.parse import quote as urlquote

from . import _vendor.six.moves.urllib.parse import unquote as urlunquote

from . import _
