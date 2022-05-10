import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r' + '     '), daemon=True).start()
for i in range(5):
    print(i)
    time.sleep(0.5)

# Output
#     1234

# We are using threading to print the space characters and move the cursor to the
# beginning of the line. The target function has been defined as a lambda function
# because it does not require any arguments. You can also use a normal function definition
# with the threading.Thread constructor.

# The output of this program has the cursor at the beginning of the line, and the
# space characters overwrite the previous outputs. The first output has a cursor at
# the end of the line, but the rest of the output has the cursor at the beginning of
# the line.

# The threading module provides many other methods and arguments. You can read
# about them in the official Python documentation.

# A thread is basically a sequence of such instructions that execute
# independently and can be interleaved with the execution of other threads.
# Although this might seem like a simple concept, there is a lot of complexity

