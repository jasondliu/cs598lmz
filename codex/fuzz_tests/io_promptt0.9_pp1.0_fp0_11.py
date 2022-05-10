import io
# Test io.RawIOBase too to get code coverage.
import io
class NullStream(io.RawIOBase):
  """A stream that discards all inputs and never blocks."""
  def write(self, buf):
    return len(buf)
  def read(self, size=-1):
    return python_bytes()
  def flush(self):
    pass



def print_to_stderr(msg):
  print(msg, file=sys.stderr)

# We need to fool some imports so the external libraries don't crash,
# because we are not even running on a computer.
class ModuleMock():
  def __getattr__(self, name):
    return ModuleMock()

  def __call__(self, *args, **kwargs):
    return ModuleMock()

  def __enter__(self):
    return ModuleMock()

  def __exit__(self, exc_type, exc_value, traceback):
    pass

# 'thread' has some side effects when imported: it sets the '_thread' module.
import sys as _sys
_sys.
