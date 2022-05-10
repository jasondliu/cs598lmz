import io
# Test io.RawIOBase
print(io.RawIOBase.seek.__doc__)
# Test io.BufferedIOBase
print(io.BufferedIOBase.tell.__doc__)

# Test typing.List
from typing import List
print(List.append.__doc__)

# Test numpy.ndarray
import numpy as np
print(np.ndarray.copy.__doc__)
