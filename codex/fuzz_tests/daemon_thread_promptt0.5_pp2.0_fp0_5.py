import threading
# Test threading daemon mode
# https://docs.python.org/3.4/library/threading.html#thread-objects
# A thread can be flagged as a "daemon thread". The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property.
#
# This is used in the following way:
#
#     Start a new thread.
#     Set the daemon flag to True.
#     Do other stuff.

# This is useful to have long-running threads that should not prevent the program to exit if all non-daemon threads have exited.
#
# Note that it is not possible to reliably detect daemon threads. For example, the threading module provides the isDaemon() method which can be used to determine if a thread is a daemon thread or not, but this method can return False even if the thread is a daemon thread (if the daemon flag has not been set yet).
#
# Also note that daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.) may not be released properly. If you want your
