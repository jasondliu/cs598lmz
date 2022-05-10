import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The default encoding for the system.
default_encoding = sys.getdefaultencoding()

# The preferred encoding for the system.
preferred_encoding = locale.getpreferredencoding()

# The filesystem encoding for the system.
filesystem_encoding = sys.getfilesystemencoding()

# The encoding used by the C runtime.
c_runtime_encoding = 'mbcs' if sys.platform == 'win32' else None

# The default encoding used by Python.
python_default_encoding = 'utf-8'

# The default encoding used by Python on Windows.
python_default_windows_encoding = 'utf-8'

# The default encoding used by Python on non-Windows.
python_default_non_windows_encoding = 'ascii'

# The default encoding used by Python on OSX.
python_default_osx_encoding = 'utf-8'

# The default encoding used by Python on Linux.
python_default_linux_encoding = 'ascii'

