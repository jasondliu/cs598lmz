fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# bpo-36410: Workaround for the bug in CPython 3.8
# (https://bugs.python.org/issue36410).
#
# The bug was fixed in Python 3.9.
#
# This test must be run in a separate process because it crashes the interpreter.

import sys
from test import support

if sys.version_info < (3, 9):
    support.run_unittest(support.CrashTest)
