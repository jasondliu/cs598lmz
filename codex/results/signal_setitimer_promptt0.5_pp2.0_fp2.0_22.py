import signal
# Test signal.setitimer
import socket
import sys
import threading
import time
import traceback

from test import support

# Test whether the interval timer works.
# The test takes about TIMER_TEST_TIME seconds.
TIMER_TEST_TIME = 5.0

# Time to wait for threads to finish in join() calls.
JOIN_TIMEOUT = 5.0

# Test whether the realtime timer works.
# The test takes about RT_TIMER_TEST_TIME seconds.
RT_TIMER_TEST_TIME = 5.0

# Time to wait for threads to finish in join() calls.
JOIN_TIMEOUT = 5.0

# The timeout for socket operations.
SOCKET_TIMEOUT = 2.0

# The time to wait for a thread to start.
START_TIMEOUT = 2.0

# The number of times to repeat the test.
COUNT = 10

# The number of threads to use for the test.
THREADS = 10

# The number of pending connections the server socket is set to.
BACKLOG = 5


