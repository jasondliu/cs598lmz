import signal
# Test signal.setitimer() and signal.getitimer().
# XXX: coverage.py hangs when using signal.setitimer() and signal.getitimer()
# under coverage measurement.
# This is a known issue: http://bitbucket.org/ned/coveragepy/issue/85/cant-use-setitimer-or-alarm-in-measurements
