import select
# Test select.select([], [], [], 0.0) behaviour when there is no FD_CLOEXEC.
# https://bugs.python.org/issue30575

# This test fails on systems with broken select.select which is the case on
# some systems like mips64el which still have this bug:
# https://sourceware.org/bugzilla/show_bug.cgi?id=7015

import os
import selectors
import subprocess
import sys
import time
import unittest

try:
    select.select([], [], [], 0.0)
except select.error as ex:
    if ex.errno != errno.EBADF and ex.errno != errno.EINVAL:
        raise
    raise unittest.SkipTest("select is broken")

import test.support

# This test is useless on Android because we never fork processes there.
