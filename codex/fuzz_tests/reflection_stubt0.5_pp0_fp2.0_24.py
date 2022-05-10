fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This should raise a TypeError.
with self.assertRaises(TypeError):
  fn()
"""

  def test_code_object_with_func_type(self):
    with self.assertRaises(TypeError):
      self.Check("""
def fn():
  pass

fn.__code__ = type(fn)

# This should raise a TypeError.
fn()
""")

  def test_code_object_with_invalid_code(self):
    with self.assertRaises(TypeError):
      self.Check("""
def fn():
  pass

fn.__code__ = "invalid"

# This should raise a TypeError.
fn()
""")

  def test_code_object_with_invalid_code2(self):
    with self.assertRaises(TypeError):
      self.Check("""
def fn():
  pass

fn.__code__ = 1

# This should raise a TypeError.
fn()
""
