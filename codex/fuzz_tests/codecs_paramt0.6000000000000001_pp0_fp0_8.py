import codecs
codecs.register_error('decomposite', decomposite)

# Default encoding for text files.
defaultencoding = 'utf-8'

# The encoding of the user's console.
consoleencoding = None

# The encoding of the user's locale.
localeencoding = None

# The encoding of the filesystem.
filesystemencoding = None

# The default encoding to use for the console.
# This is used to initialize the consoleencoding.
# This can be changed by the user with the -C command-line option.
defaultconsoleencoding = None

# The default encoding to use for the locale.
# This is used to initialize the localeencoding.
# This can be changed by the user with the -C command-line option.
defaultlocaleencoding = None

# The default encoding to use for the filesystem.
# This is used to initialize the filesystemencoding.
# This can be changed by the user with the -C command-line option.
defaultfilesystemencoding = None

# The default encoding to use for the editor.
# This is used to initialize the editor.encoding option.

