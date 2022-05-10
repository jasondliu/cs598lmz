import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath, exists

from os \
    import makedirs, listdir, remove

from subprocess \
    import Popen, PIPE

from sys \
    import argv, exit

from time \
    import time

from traceback \
    import print_exc

from types \
    import StringType

from xml.dom.minidom \
    import parseString

from xml.parsers.expat \
    import ExpatError

from zipfile \
    import ZipFile

from zipfile \
    import ZIP_DEFLATED

from zipfile \
    import ZIP_STORED

from zipfile \
    import ZIP_BZIP2

from zipfile \
    import ZIP_LZMA

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the file containing the version information:
VersionFile = 'version.txt
