fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a regression test for a bug in the optimization of
# list comprehensions.  This used to fail with a SystemError.
print([x for x in [1, 2, 3] if x > 2])

# Regression test for a bug in the code that handles the "else" clause
# of a for loop.
for i in range(5):
    break
else:
    print("else")

# Regression test for a bug in the code that handles the "else" clause
# of a while loop.
while False:
    break
else:
    print("else")

# Regression test for a bug in the code that handles the "else" clause
# of a try/except.
try:
    raise IndexError
except IndexError:
    pass
else:
    print("else")

# Regression test for a bug in the code that handles the "else" clause
# of a try/finally.
try:
    pass
finally:
    pass
else:
    print("else")

# Regression test for a bug in
