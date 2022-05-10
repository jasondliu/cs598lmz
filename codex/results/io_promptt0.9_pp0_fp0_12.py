import io
# Test io.RawIOBase doesn't give an infinite recursion.
#import locale
# Test locale.Error, locale.setlocale, locale.localeconv don't give infinite recursion.
#import mmap
# Test mmap.error doesn't give an infinite recursion.
#import ntpath
# Test ntpath.Error, ntpath.abspath, ntpath.abspath, ntpath.pathsep, ntpath.devnull, ntpath.realpath, ntpath.relpath don't give infinite recursion.
#import nturl2path
# Test nturl2path.pathname2url, nturl2path.url2pathname don't give infinite recursion.
#import os
# Test os.altsep, os.altsep, os.curdir, os.curdir, os.environ, os.linesep, os.linesep, os.pardir, os.pardir, os.pathsep, os.pathsep, os.sep, os.sep, os.path don't give infinite recursion.
#import os
