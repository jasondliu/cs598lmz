fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# >> RuntimeError: generator raised StopIteration

# when the python interpreter executes a callable (e.g. a function or a callable object), 
# it first checks the type of the object, 
# then selects an appropriate header, and then calls the call slot.
# The header decides the runtime behavior (for example, calling a type). 
# We can take advantage of that to create a function that changes behavior midflight.

# Set its code on-the-fly to a coroutine function.
>>> def power(x):
...     p = 1
...     for i in range(x):
...         yield p
...         p *= 2
...
>>> fn.__code__ = power(4).__code__
>>> fn()
1
2
4
8
# fn is now a power of two generator!


# Example of V-table
def py_dictiter(d):
    it = d.iter()
    while 1:
        try:
            yield it.next()
        except StopIteration:
            break

def py_setiter(s
