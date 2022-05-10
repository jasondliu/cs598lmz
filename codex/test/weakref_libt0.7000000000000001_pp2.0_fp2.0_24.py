import weakref
import traceback

# check for pyqt
try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

#-------------------------------------------------------------------------------
# Commonly used status codes
#-------------------------------------------------------------------------------

# add a shortcut for various statuses
OK = 200

#-------------------------------------------------------------------------------
# Commonly used content types
#-------------------------------------------------------------------------------

# add a shortcut for various content types
JSON = 'application/json'
XML = 'application/xml'

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

# add a shortcut for various content encoding
GZIP = 'gzip'

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

# add a shortcut for various content charset
UTF8 = 'utf-8'

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

# add a shortcut for various content compression
COMPRESSION = 'compression'

#
