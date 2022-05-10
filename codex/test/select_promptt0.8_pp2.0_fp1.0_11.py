import select
# Test select.select, select.poll and select.epoll
#
# Note: epoll only works on a 2.6 or better kernel.
#
# Usage: python select_tests.py [<test name>]
# where <test name> can be
#      * (the default) to run all tests
#      * select to run all tests using select
#      * poll to run all tests using poll
#      * epoll to run all tests using epoll
#      * select_error to run tests for select error handling
#      * poll_error to run tests for poll error handling
#      * epoll_error to run tests for epoll error handling
#      * select_xxx to run test xxx using select
#      * poll_xxx to run test xxx using poll
#      * epoll_xxx to run test xxx using epoll
#
# Example:
#   python select_tests.py epoll_sendfile
# to run the sendfile test using epoll.

# Much of the code below was taken from Lib/test/test_socketserver.py

from test import test_support
