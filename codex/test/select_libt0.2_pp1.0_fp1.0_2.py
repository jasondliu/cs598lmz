import select
import sys
import time

import pytest

from . import utils

# This is a list of all the tests that are expected to fail.
# The test will be marked as expected failure.
# The test will be run, but the failure will not cause the test suite to fail.
#
# The format of the list is:
#   [ (test_name, reason), ... ]
#
# The test_name is the name of the test function.
# The reason is a string that will be printed out when the test fails.
#
# If you add a test to this list, you must also add it to the list of tests
# in the file 'expected_failures.txt'.
#
# If you remove a test from this list, you must also remove it from the list
# of tests in the file 'expected_failures.txt'.
#
# If you modify the reason for a test, you must also modify the reason in the
# file 'expected_failures.txt'.
#
# If you add a test to this list, you must also add it to the list of tests
