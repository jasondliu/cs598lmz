import mmap
# Test mmap.mmap blocking behaviour

# Python 2.4
#   >     a = mmap.mmap(1,1)
#   >     a.write("x")
#   >     a.read()
#   'x'

# Python 2.5 and Python 3.0
#   >     a = mmap.mmap(1,1)
#   >     a.write("x")
#   >     a.read()
#   Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "mmap.py", line 152, in read
#       return f.read(size)
#     TypeError: must be read-write buffer, not readonly buffer

#   >     a = mmap.mmap(1,1)
#   >     a.write("x")
#   >     a.readline()
#   'x'

#   >     a = mmap.mmap(1,1)
#   >     a.write("x")
#   >     a.readlines()

