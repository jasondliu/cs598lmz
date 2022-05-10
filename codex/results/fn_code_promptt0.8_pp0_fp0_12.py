fn = lambda: None
# Test fn.__code__.co_code
print("Testing function with empty fn.__code__.co_code...")
fn.__code__.co_code = bytearray()

try:
  disassemble(fn)
except ValueError:
  print("Successfully raised ValueError")
else:
  print("Expected to raise ValueError")

# Test fn.__code__.co_code with no instructions
print("Testing function with fn.__code__.co_code with no instructions...")
fn.__code__.co_code = bytearray([0, 0])

try:
  disassemble(fn)
except ValueError:
  print("Successfully raised ValueError")
else:
  print("Expected to raise ValueError")

# Test fn.__code__.co_code with no instructions and some argument values
print("Testing function with fn.__code__.co_code with no instructions and some arguments...")
fn.__code__.co_code = bytearray([0, 1, 0, 0, 0, 0])

try:
  disas
