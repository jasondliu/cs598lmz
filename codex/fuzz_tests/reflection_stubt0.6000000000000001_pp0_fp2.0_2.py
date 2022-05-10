fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
'''

# Recursive function
def run(n):
    if n == 0:
        return
    else:
        run(n-1)
        print (n)

run(3)

# Function, with default arguments
def run(n=3):
    if n == 0:
        return
    else:
        run(n-1)
        print (n)

run()

# Function, with parameters
def run(n=3):
    if n == 0:
        return
    else:
        run(n-1)
        print (n)

run(5)

# Function, with variable arguments
def run(*args):
    if len(args) == 0:
        return
    else:
        print (args[0])
        run(*args[1:])

run(1,2,3,4)

# Function, with keyword arguments
def run(**kwargs):
    if len(kwargs) == 0:
        return
    else:
        for k,v
