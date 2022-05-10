gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)  # <code object <genexpr> at 0x00000178D8E6E2D0, file "<stdin>", line 1>
# ... and gi.gi_frame
print(gi.gi_frame)  # <frame object at 0x00000178D8EDAF38>
# This is a bit much.
"""
Do not use the gi_frame attribute to access or modify the local variables or
stack of the generator!  The implementation of this attribute is highly
version-dependent, and accessing or modifying its contents is likely to crash
the interpreter.
"""

"""
The next() function can be used to control generator execution (see also the
section Control Flow).
"""
# The next(...) function:
def squares(start, stop):
    for i in range(start, stop):
        yield i ** 2


for i in squares(1, 5):
    print(i, end=' ')  # 1 4 9 16
# It is equivalent to:
sq = squares(1, 5)
print(next(sq))  # 1
print
