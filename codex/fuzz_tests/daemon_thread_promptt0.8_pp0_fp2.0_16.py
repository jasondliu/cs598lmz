import threading
# Test threading daemon
#
#   When the main thread exits, it is system defined whether the other threads
#   continue to run. Current versions of Python behave as follows:
#
#       * In CPython, due to the Global Interpreter Lock, only one thread runs at
#         once. The others are put on hold.
#       * In PyPy, since there is no GIL, all threads are run in parallel, though
#         the exact scheduling behavior varies across platforms, and even between
#         different versions of PyPy.
#
#   In either case, the daemon threads are killed once the main thread
#   terminates.
#
#   Note that a daemon thread cannot be a program's main thread.
#
#   Daemon threads should also not access Python objects other than their
#   own local data in daemons (shared data is not safe).
#
def worker():
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    threads.append(t)
    t
