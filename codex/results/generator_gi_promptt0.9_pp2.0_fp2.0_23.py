gi = (i for i in ())
# Test gi.gi_code is None to recognize the default argument clause::
#
#   def f(a=None):
#       ...
#
# We need to explicitly test that gi_code is None because in functions defined
# in python modules the generator may already exist (it is not None) and thus
# we need to check that it is not.
a = (1,)
while a is not None:  # type: ignore
    if gi.gi_code is None:
        break
    a = a[0]

del a, gi

try:
    try:
        1.0 + True  # type: ignore
    except True as e:
        pass
except TypeError as e:
    try:
        1.0 + False  # type: ignore
    except False as e:
        pass
except TypeError as e:
    try:
        1.0 + Fals
