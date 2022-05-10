import _struct as struct

from pyblish import api
from pyblish.util import os as pyblish_util_os

if hasattr(sys, 'frozen'):
    # py2exe
    #
    # Paths are relative to the executable
    #
    # I.e. "C:\Program Files\Autodesk\Maya2017\bin\maya.exe"
    # Note: Maya is installed in the `bin` directory
    #
    # _base = os.path.dirname(sys.executable)
    #
    # But we want it to be relative to "C:\Program Files\Autodesk\Maya2017\"
    #
    _base = os.path.dirname(os.path.dirname(sys.executable))

else:
    # Standalone installation
    #
    # Paths are relative to the root of the plugin
    #
    # I.e. "C:\Program Files\Autodesk\Maya2017\plug-ins\pyblish.bundle"
    #
    _base = os.path.dirname
