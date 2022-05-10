import io
# Test io.RawIOBase.
with io.StringIO() as f:
  print(f)


class AIO:
  @property
  def f(self) -> int:
    return 0

# Test the __aenter__ @property annotation.
with AIO() as a:
  print(a)

# Test optional @property annotations.
class OptionalProperty:
  @property
  def optional(self) -> Optional[int]:
    return None
  @optional.setter
  def optional(self, value: Optional[int]):
    pass

# Test the annotation on __repr__.
class Repr:
  def __repr__(self) -> str:
    return "Hello"

# Test the annotation on __str__.
class Str:
  def __str__(self) -> str:
    return "Hello"

class Subclassable:
  def __init_subclass__(cls: type) -> None:
    pass

# Test the annotation on __format__.
class Format:
  def __format__(self, format_spec: str) -> str
