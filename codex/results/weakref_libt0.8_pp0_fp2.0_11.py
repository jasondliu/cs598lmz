import weakref
import sys
import os
import struct
import platform
import tempfile
import mmap

import mutagen
from mutagen._compat import iteritems, cBytesIO
from mutagen._compat import text_type, PY3, PY2, WIN, xrange
from mutagen._util import (load_after, cdata, DictProxy, typeof, DictProxy,
                           load_module_safely)
from mutagen.mp3 import error as MP3Error
from mutagen.apev2 import error as APEv2Error
from mutagen.oggspeex import OggSpeex, OggSpeexHeaderError
from mutagen.oggtheora import OggTheora, OggTheoraHeaderError


__all__ = ["Open", "File", "FileType", "HeaderNotFoundError",
           "rate_to_string", "string_to_rate", "string_to_size", "ERROR",
           "BIN", "EXTENSION"]

EXTENSION = 0
BIN = 1
ERROR = 2

MUTAGEN_MAPPING = {

