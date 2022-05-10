fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Output:
# Traceback (most recent call last):
#   File "python", line 5, in <module>
# TypeError: 'generator' object is not callable

# Example 2
fn = lambda: None
fn.__code__ = 1
fn()

# Output:
# Traceback (most recent call last):
#   File "python", line 5, in <module>
# TypeError: 'int' object is not callable
