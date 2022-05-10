import lzma
lzma_comp = lzma.compress
lzma_decomp = lzma.decompress
# end pyflakes

from .. import version

from bytesio import BytesIO
from debug import debug, debug_exc, assert_debug
from encoding import default_encoding
from events import Event
from files import FilePath, FilePath_from_unicode
from interfaces import IFilePath
from logs import Logger
from options import Options
from osutils import _get_encoding
from path import path
from posixpath import join as join_posix
from tempfile import TemporaryFile
from threading import Condition, Lock, Thread
from transform import (
    Transform,
    TransformChain,
    TransformFactory,
    TransformException,
    )
from url import URL
from weakutil import WeakValuedCache
from worker import WorkerQueue
from zippath import ZipPath

if str == bytes:
    def as_str(s):
        return s
else:
    def as_str(s):
        return s.decode('ascii')

def split_leading_dir
