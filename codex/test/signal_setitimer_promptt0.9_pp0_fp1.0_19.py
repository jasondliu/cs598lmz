import signal
# Test signal.setitimer, Unix only.
# Make sure a signal occurs in at most 1 second.
import os, sys, signal, traceback, time

timeout = 1.0

