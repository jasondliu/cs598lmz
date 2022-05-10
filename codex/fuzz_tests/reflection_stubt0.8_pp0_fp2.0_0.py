fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class Foo(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Bar(object):
  def __init__(self, z):
    self.z = z


def get_data(x):
  if x == 0:
    return Foo(1, 2)
  elif x == 1:
    return Bar(2)
  else:
    return None


def main():
  for i in range(10):
    data = get_data(i)
    if data:
      if isinstance(data, Foo):
        print data.x, data.y
      elif isinstance(data, Bar):
        print data.z
  return 0

main()
