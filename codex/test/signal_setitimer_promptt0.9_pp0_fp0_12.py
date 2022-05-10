import signal
# Test signal.setitimer() with a relative expiration (time until SIGALRM)
# The test process should exit before the alarm is delivered.
#
# This test program replaces alarm() in the config.status script of GCC,
# and is used by configure.py

