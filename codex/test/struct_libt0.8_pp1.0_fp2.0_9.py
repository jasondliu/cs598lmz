import _struct
import _sys
import _thread
import _time
import _threading
import _tkinter
import _turtle
import _ttk
import _types
import _ui
import _unittest
import _urllib
import _uuid
import _virtualenv
import _wave
import _webbrowser
import _webkit
import _winreg
import _winsound
import _wmi
import _xml
import _xmlrpc
import _zipfile
import _zipimport
import _zlib
import _zmq

# Remove the modules from sys.modules, so attempting to import them again
# will look up the modules in sys.meta_path
for name in (name for name in sys.modules.keys() if name.startswith('_')):
	del sys.modules[name]
