import io
# Test io.RawIOBase inheritance
class SIO(io.RawIOBase):
  def readable(self):
    return True
  def readinto(self, b):
    n = len(b)
    for i in range(n):
      b[i] = i
    return n
s = SIO()
s.read(4)
# test io.RawIOBase inheritance when not overriding raw methods

def test_inner():
    class A(io.RawIOBase):
        pass
    with A() as a:
        print(a.read(5))

