import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# To be clear, this is not the recommended approach for doing I/O in Python.
#   The recommended way is to use the threading module to create multiple threads
#   that each run their own event loop, and use the signal module to signal between threads.

# This is also not a recommended way to do network programming.
#   The recommended way is to use the Twisted framework,
#   which is an event-driven networking engine written in Python.
#   Another option is to use the select() function,
#   which is a cross-platform Unix/Windows primitive for waiting on multiple I/O channels.

# The above programs may work well on some platforms,
#   but they may not work well on all platforms.
# It is possible to write programs that use the threading module to do parallel processing,
#   and also use the signal and select modules to do evented I/O,
#   but this is a complex task that
