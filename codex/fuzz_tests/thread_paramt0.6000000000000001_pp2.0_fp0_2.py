import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello, world\n")).start()

# Using a threading.Thread object, we can call the start() method to tell the interpreter to begin executing the run() method in a separate thread of control.

# Thread Objects

# The constructor for the Thread class takes a callable object and, optionally, a name for the thread as arguments.

# The callable object passed to the constructor should expect one argument. When the run() method is called, it will call the callable object with a single argument.

# If a name is not provided to the constructor, the name of the thread will be the name of the callable object.

# The run() method will call the callable object passed to the constructor and will return when the callable object returns.

# The return value of the callable object will be ignored.


# Example

# Let’s write a more complex example that uses threads to do something more useful than printing “hello, world”.

# The example below uses the threading.Thread class to implement a worker thread that takes jobs off a queue, processes them, and marks them as
