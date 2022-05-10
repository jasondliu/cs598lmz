import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# The above code will print hello, but it will not wait for the thread to finish.

# If you want to wait for the thread to finish, you can use the join() method.

import sys, threading
t = threading.Thread(target=lambda: sys.stdout.write("hello\n"))
t.start()
t.join()

# The join() method will wait for the thread to finish.

# The following example shows how to use the join() method:

import sys, threading
t = threading.Thread(target=lambda: sys.stdout.write("hello\n"))
t.start()
t.join()
print("world")

# The above example will print hello, and then wait for the thread to finish.
# When the thread has finished, it will print world.

# The following example shows how to use the join() method to wait for a thread to finish:

import sys, threading
