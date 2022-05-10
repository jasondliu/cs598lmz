import signal
# Test signal.setitimer
#
# From APUE:
# The following program demonstrates the use of setitimer to generate a
# SIGALRM signal once a second. It also illustrates the use of the SA_RESTART
# flag with sigaction so that read doesn't fail when the SIGALRM signal is
# caught.
import sys
import time

