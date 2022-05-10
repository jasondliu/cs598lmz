import io
# Test io.RawIOBase.
with io.StringIO() as f:
  print(f)


class AIO:
  @property
  def f(self) -> int:
    return 0

# Test the __aenter__ @property annotation.
