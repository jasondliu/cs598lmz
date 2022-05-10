import ctypes
ctypes.cast(1, ctypes.py_object)

# Slicing: we can obtain new tuples with only a portion of the elements.

t = (1, 2, 3, 4, 5, 6)
t[1:3]
t[1:-1]
t[0:3]
t[:3]
t[3:]
t[:]

# We can also define the step of the slice.

t[::2]
t[1::2]

# Tuples support concatenation.

(1, 2, 3) + (4, 5, 6)

# And repetition.

('Hi!',) * 4

# Like strings, tuples are immutable.

t = (1, 2, 3)
