import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# The point of this example is to show how slow the
# select.select() call is.

# If you try to run this code on a Mac OS X machine,
# you might notice that it runs very fast. This is likely
# because Mac OS X has a very efficient implementation of
# select(). On Linux, the average time per call is 0.05 seconds.

# On Mac OS X, the average time per call is 0.0005 seconds.

# So, depending on your operating system, the results may
# vary.

# The important thing to notice is that the slow_systemcall()
# function executes in about the same amount of time,
# no matter how many times it is called.

# The select() function is a direct interface to the Unix
# system call of the same name.
