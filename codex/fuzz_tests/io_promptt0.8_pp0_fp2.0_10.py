import io
# Test io.RawIOBase
print(io.RawIOBase.read.__doc__)

# Test io.BufferedIOBase
print(io.BufferedIOBase.read.__doc__)

# Test io.TextIOBase
print(io.TextIOBase.readline.__doc__)


import numbers
# Test numbers.Number
print(numbers.Number.__add__.__doc__)

# Test numbers.Complex
print(numbers.Complex.conjugate.__doc__)

# Test numbers.Real
print(numbers.Real.is_integer.__doc__)

# Test numbers.Rational
print(numbers.Rational.__format__.__doc__)

# Test numbers.Integral
print(numbers.Integral.__floordiv__.__doc__)


"""
import collections.abc
# Test collections.abc.Container
print(collections.abc.Container.__contains__.__doc__)

# Test collections.abc.Hashable
print(collections.abc.Hashable.__hash__.__doc__
