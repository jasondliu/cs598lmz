fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# Test fn.__code__.co_name
print(fn.__code__.co_name)

def outer():
  x = 1
  def inner():
    print(x)
  return inner
fn = outer()
# Test fn.__code__.co_freevars
print(fn.__code__.co_freevars)
# Test fn.__closure__
print(fn.__closure__)

# Test class property
class A:
  @property
  def fn(self):
    print(self)
A().fn

# Test class method
class B:
  @classmethod
  def fn(cls):
    print(cls)
B.fn()

# Test staticmethod
class C:
  @staticmethod
  def fn():
    print(C)
C.fn()
