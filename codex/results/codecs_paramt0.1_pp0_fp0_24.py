import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a hack to make sure that the right version of
# pywin32 is imported.  This is necessary because the pywin32
# installer is broken and does not install the pywin32 package
# in the right place.
#
# The following code is based on the code in the pywin32 installer
# (pywin32-214.win32-py2.7.exe) in the file pywin32_postinstall.py.
#
# The code in the installer is broken because it does not take into
# account the fact that the pywin32 package may already be installed
# in the system Python.  If it is, then the pywin32 package in the
# system Python will be imported instead of the one in the virtualenv.
#
# The following code fixes this problem by removing the pywin32
# package from the system Python.

import sys
import os
import shutil

def remove_pywin32_from_system_python():
    # Remove the pywin32 package from the system Python.
    #
    # This is necessary because
