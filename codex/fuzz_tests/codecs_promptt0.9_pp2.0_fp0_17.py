import codecs
# Test codecs.register_error('ignore')
import ctypes
# Test ctypes.PyArg_ParseTupleAndKeywordsFails
import doctest
import encodings
# Test encodings.utf_8.register_error('ignore')
import io
import os
import select
# Test  'select'module Py_FILE_INPUT/OUTPUT
import subprocess
# Failed if subprocess.call(['cat','badfilename']) not failed
import tempfile
# Test error on open bad filename
import threading
# Test error on run function
import unittest
import xmlrpc.client
#
