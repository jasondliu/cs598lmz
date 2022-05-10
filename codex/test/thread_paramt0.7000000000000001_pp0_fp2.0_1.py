import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

# The following code will fail with a "maximum recursion depth exceeded" error
def f():
    f()
f()

# The following code will fail with a "maximum recursion depth exceeded" error
def f():
    g()
def g():
    f()
f()

# The following code will fail with a "maximum recursion depth exceeded" error
def f(x):
    return f(x)
f(1)

# The following code will fail with a "maximum recursion depth exceeded" error
def f(x):
    return g(x)
def g(x):
    return f(x)
f(1)

# The following code will fail with a "maximum recursion depth exceeded" error
def f(x):
    return f(f(x))
f(1)

# The following code will fail with a "maximum recursion depth exceeded" error
def f(x):
    return g(g(x))
def g(x):
    return f(f(x))
f(1)


