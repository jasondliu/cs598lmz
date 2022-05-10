import weakref

from . import _common, _compat
from ._common import _DummyFile
from ._compat import _basestring, _long, _unicode, _callable, _bytes, _text_type
from ._compat import _PY2, _PY3, _PY34, _PY35, _PY36, _PY37, _PY38, _PY39
from ._compat import _WIN, _POSIX, _OSX
from ._compat import _os_fspath, _os_fdopen, _os_open, _os_close
from ._compat import _os_pipe
from ._compat import _subprocess_open, _subprocess_call, _subprocess_check_output
from ._compat import _subprocess_Popen, _subprocess_STDOUT, _subprocess_DEVNULL
from ._compat import _subprocess_CalledProcessError
from ._compat import _subprocess_TimeoutExpired
from ._compat import _subprocess_list2cmdline
from ._compat import _subprocess_mswindows
from ._comp
