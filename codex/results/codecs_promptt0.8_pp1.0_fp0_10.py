import codecs
# Test codecs.register_error
import _codecs
# Imports for test_import
import sys, imp, os, stat, shutil, time, struct, tempfile
import re
import unittest
import pkgutil, test.test_pkgutil
import test.support
if test.support.verbose:
    import pprint
# Imports for test_support_code_type
import dis, pickle
import types, builtins
# Imports for test_sys_settrace
import sys
import _testcapi
# Imports for test_silly_getattr
import sys
# Imports for test_str_signature
import inspect, textwrap
# Imports for test_StringIO
import io, sys
# Imports for test_marshal
import io, types, marshal, pickle
import unittest.test.testmarshal
# Imports for test_re
import re, unittest
# Imports for test_record
import unittest, sys
# Imports for test_cmath
import unittest, cmath
# Imports for test_pow
import unitt
