fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Should print:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <lambda>
# TypeError: 'generator' object is not callable

# But instead it prints:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <lambda>
# TypeError: 'generator' object is not callable

# In Python 2.7.15, the following code works fine.
# In Python 3.7.0, the following code works fine.
# In Python 3.8.0, the following code works fine.
#
# The above code is a simplified version of this code:
#
# class C(object):
#     @staticmethod
#     def f():
#         pass
#
# c = C()
# c.f = (i for i in ())
# c.f()
#
# In Python 2.7
