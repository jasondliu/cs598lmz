import signal
# Test signal.setitimer for the alarm() function.
#
# Written by Moses DeJong in May 2008.
#
# This module is in the public domain.
#
# Usage: python t_sigalarm.py
#
# We run t_sigalarm in a bg script because it is
# very hard to get timeout support working correctly
# on all platforms.  In particular, Python itself
# uses SIGALRM in threading.py and it is not always
# safe to catch that signal.  The bg script ensures
# that a second Python process will not be affected
# by the t_sigalarm test.

import sys
import os
import time
import signal

tm_sec = 0
tm_usec = 500000 # .5 seconds

def alarm_handler(signo, frame):
  global tm_sec
  tm_sec += 1

def sigsetitimer_test():
  # verify that sigprocmask() works with SIG_SETMASK, SIG_BLOCK and SIG_UNBLOCK

  if hasattr(signal, "SIGUSR1"):
