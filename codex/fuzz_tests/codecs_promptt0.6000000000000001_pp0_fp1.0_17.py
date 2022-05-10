import codecs
# Test codecs.register_error
import errno
import glob
import os
import shutil
import signal
import stat
import sys
import tempfile
import time
import traceback

from test import support
from test import script_helper

# Skip these tests if there is no os.fork().
if not hasattr(os, 'fork'):
    raise unittest.SkipTest("os.fork not defined")

# Skip these tests if the default directory is not writable
if not os.access(os.curdir, os.W_OK):
    raise unittest.SkipTest("Current directory not writable")

# Skip these tests if os.execv is not available
if not hasattr(os, 'execv'):
    raise unittest.SkipTest("os.execv not defined")

# Skip these tests if the os module does not have a kill function
if not hasattr(os, 'kill'):
    raise unittest.SkipTest("os.kill not defined")

# Skip these tests if os.kill is not available
if hasattr(signal, 'SIGKILL'):
