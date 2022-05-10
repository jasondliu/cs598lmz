import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists, dirname, basename, splitext, isdir, isfile, abspath

from os \
    import makedirs, listdir, walk, remove, rmdir, rename

from os \
    import environ

from os.path \
    import normpath, normcase

from os.path \
    import curdir, pardir, sep, pathsep, altsep, extsep, devnull

from os.path \
    import commonprefix

from os.path \
    import splitdrive, split, splitext, splitunc, drive, isabs, basename, \
           dirname, join, islink, lexists, exists, isdir, isfile, getsize, \
           getmtime, getatime, getctime, ismount, walk, expanduser, expandvars

from os.path \
    import abspath, realpath, relpath

from os.path
