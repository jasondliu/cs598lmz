import lzma
lzma.__doc__

try:
    import bz2
    bz2.__doc__
except ImportError:
    _have_bz2 = False
else:
    _have_bz2 = True

try:
    import lzma
    lzma.__doc__
except ImportError:
    _have_lzma = False
else:
    _have_lzma = True


# At the moment, I believe the best way to detect whether or
# not we have lz4 support is to attempt to import the extension
# and then check for the exception it raises.
#
# The problem is that pylz4 is not installable with pip, and
# the only way to install it is to clone the repository and
# run setup.py. But, this results in the setup.py script checking
# for the lz4 library and failing if it is not found.
#
# So, we have to trick it into thinking it can build the library
# even if we don't have it and then handle the exception.
#
# Importing the extension will fail if we
