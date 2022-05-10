import _struct
import _thread
import _threading
import _time
import _timeit
import _token
import _tokenize
import _traceback
import _tracemalloc
import _tty
import _turtle
import _turtledemo
import _types
import _typing
import _unittest
import _urllib
import _uu
import _uuid
import _venv
import _warnings
import _wave
import _weakref
import _webbrowser
import _winreg
import _winsound
import _wsgiref
import _xdrlib
import _xml
import _xmlrpc
import _zipapp
import _zipfile
import _zipimport
import _zlib

# These modules are not built on Windows.
if not sys.platform.startswith('win'):
    import _testcapi
    import _tkinter

# These modules are not built on Windows and Mac OS.
if not sys.platform.startswith(('win', 'darwin')):
    import _multiprocessing
    import _posixsubprocess
   
