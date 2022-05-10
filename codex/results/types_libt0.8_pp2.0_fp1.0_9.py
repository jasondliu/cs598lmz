import types
types.ClassType = types.TypeType

def function(arg):
  if type(arg) is type(lambda: None):
    f = arg
  else:
    def f(*args, **kwargs):
      return arg(*args, **kwargs)
  return f

class To_str(object):
  def __str__(self):
    return self.to_str()

if __name__=='__main__':
  from libtbx.test_utils import approx_equal
  assert approx_equal(det(matrix.sqr((1, 2, 3, 4))), -2)
  assert approx_equal(det(matrix.sqr((1, 2, 3, 4, 5, 6, 7, 8, 9))), 0)
  assert approx_equal(det(matrix.sqr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])), 0)
  assert approx_equal(det(matrix.sqr([[1, 2, 3], [4, 5, 6], [7, 8, 1]]
