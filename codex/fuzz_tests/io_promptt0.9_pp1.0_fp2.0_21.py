import io
# Test io.RawIOBase.truncate
# pyston change: add some assertions since this tests an abstract method
try:
  f = io.RawIOBase()
  f.truncate()
  assert False, "exception not thrown"
except:
  f.truncate(5)
  assert False, "exception not thrown"

 # Test io.RawIOBase.read1
 # pyston change: add some assertions since this tests an abstract method
try:
  f = io.RawIOBase()
  f.read1()
  assert False, "exception not thrown"
except:
  f.read1(5)
  assert False, "exception not thrown"

# Test io.BufferedIOBase.peek
# pyston change: add some assertions since this tests an abstract method
try:
  f = io.BufferedIOBase()
  f.peek()
  assert False, "exception not thrown"
except:
  f.peek(5)
  assert False, "exception not thrown"

# pyston change: io.IOBase not defined in pyston
