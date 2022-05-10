import threading
# Test threading daemon default behaviour
thread = threading.Thread(target=lambda: 1 + 1)
# It will work as normal thread, program execution continues with main thread,
# until threadDie is alive
thread.threadDie = threading.Thread(target=lambda: 1 + 1)
thread.threadDie.start()
# Prints False, no thread is daemon
print(thread.threadDie.daemon)
# Make thread daemon
thread.threadDie.daemon = True
# Prints True, thread is daemon
print(thread.threadDie.daemon)
# thread is terminated
thread.threadDie.join()
# Test threading daemon on main thread
thread = threading.Thread(target=lambda: 1 + 1)
print(thread.daemon)
# Will not work, because all threads in Python created as non daemon,
# even main one
thread.daemon = True
print(thread.daemon)
thread.start()
thread.join()

# Threading Examples
# When working with threading in Python, there are several different
# patterns you might consider.
#
# Create a Thread With a Function, Using Thread
