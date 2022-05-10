fn = lambda: None
# Test fn.__code__ is an instance of types.CodeType
setattr(fn, '__code__', 42)
%timeit fn()

def fn():
    C_FUNC()

tf.autograph.experimental.set_loop_options(parallel_iterations=1)
%timeit fn()

# Let's make some control flow:

def add_one(x):
    return x+1

def mul_two(x):
    return x*2

def if_else(x):
  if x > 0:
    return add_one(x)
  else:
    return mul_two(x)

# Even in this very simple case, we still have a lot of overhead. 
# This function is 3x slower than what you'd expect with pure python.
if_else(x)

# You can speed-up with many layers of tf.function. Note you can use 
# tf.function as a decorator, or a regular function:

@tf.function
def f(x):
  return tf.function(if_else)(x)

f(
