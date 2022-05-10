import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the future!\n")).start()

time.sleep(2)

print("Hello from the past!")

# Hello from the past!
# Hello from the future!

# The code above uses threading.Thread to create a new thread that prints a message from the future.
# We then sleep for 2 seconds, and print a message from the past.
# We can see the output of both messages.

# Threads are great for I/O operations, because the operating system can schedule work on other threads while one thread is waiting for I/O.
# This is called concurrency.
# Concurrency is when two or more tasks can start, run, and complete in overlapping time periods.
# It doesn't necessarily mean they'll ever both be running at the same instant.
# Concurrency is about dealing with lots of things at once.
# Parallelism is about doing lots of things at once.

# Concurrency is about structure, parallelism is about execution.

# A thread is a single sequence of instructions within a process.
# A process is an instance of a computer program that is being
