import select
# Test select.select

# select.select([pollableobjects], [], [])
# pollableobjects is a list of objects you want to wait for input on.
# The return value is a subset of the pollableobjects that are ready for reading.

# select.select([], [pollableobjects], [])
# pollableobjects is a list of objects you want to wait for output on.
# The return value is a subset of the pollableobjects that are ready for writing.

# select.select([], [], [pollableobjects])
# pollableobjects is a list of objects you want to wait for errors on.
# The return value is a subset of the pollableobjects that have errors.

# select.select([pollableobjects], [pollableobjects], [pollableobjects])
# pollableobjects is a list of objects you want to wait for input and output on.
# The return value is a subset of the pollableobjects that are ready for reading, a subset that are ready for writing, and a subset that have errors.

# The return value is a tuple of three lists:
# rlist is a list of objects ready for reading.
