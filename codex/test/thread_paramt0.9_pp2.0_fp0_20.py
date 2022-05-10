import sys, threading
threading.Thread(target=lambda: sys.stdout.write("threading!\n"), daemon=True).start()

# This is the ____ word of the problem definition:
# "we are not constrained to using the same arguments"
#
# The function returns a function with a new argument!
#
# Using a more classical OOP/design pattern approach to this problem would lead
# to a class with a stateful __call__ method. Python does not support that, 
# because @ is a decorator, not a callable object.
#
# That said, the next best way to model it is so:

class IntClass:

  def __init__(self, arg):
    self.arg = arg

  def __call__(self, arg):
    return IntClass(self.arg + arg)

# These two functions *are* equivalent:

def add(n):
  def call(x):
    return add(x + n)
  return call

def chain(f, a):
  def chain2(f2):
    return chain(lambda x : f(f2(x)), a)
  chain
