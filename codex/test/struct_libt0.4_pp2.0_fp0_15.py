import _struct
import _thread
import _threading
import _time
import _tracemalloc
import _traceback
import _turtle
import _types
import _typing
import _unicodedata
import _unittest
import _urllib
import _uuid
import _venv
import _warnings
import _weakref
import _webbrowser
import _winreg
import _wsgiref
import _xdrlib
import _xml
import _xmlrpc
import _zipfile
import _zlib

# These modules are not available on Windows.
if not sys.platform.startswith('win'):
    import _audioop
    import _crypt
    import _fcntl
    import _multiprocessing
    import _posixsubprocess
    import _resource
    import _sre
    import _ssl
    import _tkinter

# These modules are not available on Windows and Mac OS X.
if not sys.platform.startswith(('win', 'darwin')):
    import _curses
