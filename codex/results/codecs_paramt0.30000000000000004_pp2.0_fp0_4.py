import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# This is the default encoding for the file system
# In Python 3, this is always UTF-8
# In Python 2, this is the system default encoding
default_encoding = sys.getfilesystemencoding()

# This is the default encoding for the terminal
# In Python 3, this is always UTF-8
# In Python 2, this is the system default encoding
default_terminal_encoding = sys.stdout.encoding

# This is the default encoding for the locale
# In Python 3, this is always UTF-8
# In Python 2, this is the system default encoding
default_locale_encoding = locale.getpreferredencoding()

# This is the default encoding for the operating system
# In Python 3, this is always UTF-8
# In Python 2, this is the system default encoding
default_os_encoding = os.environ.get('PYTHONIOENCODING', 'utf-8')

# This is the default encoding for the file system
# In Python 3, this is always UTF
