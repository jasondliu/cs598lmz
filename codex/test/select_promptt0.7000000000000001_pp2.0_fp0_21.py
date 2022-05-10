import select
# Test select.select() with a timeout.

# This test should be used together with test_poll.
# It should be run after test_poll.

from select import *
from test import test_support
import time, os

searcher = test_support.findfile("start.txt", subdir="select-tests")

timeout = 1

