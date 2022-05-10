import select
# Test select.select against twisted.internet.selectreactor.select()
#
# Tested on Linux 2.6.27-11-generic #1 SMP Tue Feb 10 20:59:02 UTC 2009 x86_64 GNU/Linux
#
# Twisted 8.1.0
# Python 2.5.2
#
# run like: PYTHONPATH=. ./select_select.py -v
#
# With Python 2.5.2:
# Ran 2 tests in 0.001s
# OK
#
# With Python 2.6.2:
# Ran 2 tests in 0 seconds
# OK
#
# With Python 2.6.4:
# Ran 2 tests in 0 seconds
# OK
#
# With Python 2.6.4 and selectors.poll():
# Ran 2 tests in 0 seconds
# OK
#
# With Python 2.6.4 and selectors.epoll():
# Ran 2 tests in 0 seconds
# OK
#
# With Python 2.6.4 and selectors.kqueue():
# Ran 2 tests in 0 seconds
# OK
#
# With Python 2.7
