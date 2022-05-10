import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _util
from . import _compat
from . import _exceptions
from . import _types
from . import _version
from . import _compression
from . import _constants
from . import _crc
from . import _file
from . import _filelist
from . import _filelist_unix
from . import _filelist_windows
from . import _filelist_macos
from . import _filelist_pax
from . import _fileobj
from . import _getmember
from . import _tarinfo
from . import _subprocess
from . import _tarfile
from . import _sys
from . import _os
from . import _io
from . import _path
from . import _tempfile
from . import _warnings
from . import _zipfile
from . import _zipfile_external
from . import _zipfile_stream
from . import _zipfile_stream_external
from . import _zipfile_stream_unix
from . import _zipfile_stream_windows
from . import _zipfile
