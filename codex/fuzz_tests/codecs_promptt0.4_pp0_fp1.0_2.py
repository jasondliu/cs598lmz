import codecs
# Test codecs.register_error()
import locale
import os
import re
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest
from test.support.script_helper import assert_python_ok, assert_python_failure

def get_environ():
    env = os.environ.copy()
    env['LC_ALL'] = 'en_US.UTF-8'
    return env

def get_output(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=get_environ())
    output = p.communicate()[0]
    assert p.wait() == 0
    return output

def decode_output(cmd, encoding):
    return get_output(cmd).decode(encoding)

def remove_file(filename):
    try:
        os.unlink(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

class ErrorMappingTestCase(unittest.TestCase
