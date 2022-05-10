import codecs
codecs.register_error("strict", codecs.ignore_errors)

from distutils.spawn import find_executable
import inspect
import numbers
import os
import re
import stat
import sys
import tempfile
import textwrap
import threading
import time
import traceback
import unittest
import warnings
import weakref

skip_expected_failure = unittest.skip("expected to fail")
skip_unsupported = unittest.skip("unsupported")
skip_if = unittest.skipIf
expectedFailure = unittest.expectedFailure


class TempFileMixin(object):

    def make_path(self, name):
        return os.path.join(self.environ["TMPDIR"], name)

    def make_file(self, name, content, encoding=None):
        path = self.make_path(name)
        if encoding is None:
            with open(path, "wb") as f:
                f.write(content)
        else:
            with codecs.open(path, "w", encoding=encoding) as f:
                f.write(
