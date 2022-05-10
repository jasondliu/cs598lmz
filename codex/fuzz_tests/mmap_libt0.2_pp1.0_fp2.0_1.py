import mmap
import os
import re
import sys
import time

from . import _util
from . import _winreg as winreg
from . import _winreg_py2 as winreg_py2
from . import _winreg_py3 as winreg_py3
from . import _winreg_pycompat as winreg_pycompat
from . import _winreg_testutil as winreg_testutil

if sys.version_info[0] == 2:
  import _winreg as winreg
  import _winreg_py2 as winreg_py2
  import _winreg_pycompat as winreg_pycompat
  import _winreg_testutil as winreg_testutil
else:
  import _winreg_py3 as winreg_py3
  import _winreg_pycompat as winreg_pycompat
  import _winreg_testutil as winreg_testutil


class WinRegTest(winreg_testutil.RegistryTestCase):
  """Tests for the winreg module."""

  def setUp(self):
   
