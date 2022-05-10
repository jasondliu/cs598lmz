import mmap
import os
import sys
import time

from . import _util
from ._util import _get_file_size
from ._util import _get_file_size_windows
from ._util import _get_file_size_unix
from ._util import _get_file_size_other
from ._util import _get_file_size_osx
from ._util import _get_file_size_linux
from ._util import _get_file_size_freebsd
from ._util import _get_file_size_netbsd
from ._util import _get_file_size_openbsd
from ._util import _get_file_size_solaris
from ._util import _get_file_size_aix
from ._util import _get_file_size_hpux

from ._util import _get_file_size_posix
from ._util import _get_file_size_windows_posix

from ._util import _get_file_size_posix_other
from ._util import _get_file_size_windows_posix_other

from ._util import _
