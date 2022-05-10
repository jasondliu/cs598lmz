fn = lambda: None
# Test fn.__code__.co_filename for `fn` and `instancemethod`s.
class A:
  pass
A_method = A()
A_method.fn = lambda: None
# Test fn.func_code.co_filename for unbound methods.
class B:
  fn = B
print(fn.__code__.co_filename)
print(fn.func_code.co_filename)
print(A_method.fn.__code__.co_filename)
print(A_method.fn.func_code.co_filename)
print(B.fn.__self__.__code__.co_filename)
return ""
""")
  assert ret.stdout.strip() == filename
  assert ret.returncode == 0


def test_binary_literal(test_env):
  """Test binary literals."""
  ret = test_env.run('python', '-c', r"""
print(0b10)
print(0B11)
print(0b0)
print(0B0)
# https://github.com/google/yapf/issues
