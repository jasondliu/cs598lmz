import ctypes
ctypes.cast(1, ctypes.py_object)

import numpy
numpy.int32(1)

import numpy as np
np.array([1, 2, 3])

# error: cannot import name 'Tester' from 'numpy.testing' (unknown location)
from numpy.testing import Tester
test = Tester().test

# error: Unable to import 'pandas._testing': Missing required dependencies ['numpy']
import pandas as pd
pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

import sys
import numpy as np

print(sys.version)
print(np.__version__)

import sys
import pandas as pd

print(sys.version)
print(pd.__version__)
 
# error: cannot import name 'Tester' from 'pandas.util.testing' (c:\users\user\appdata\local\programs\python\python37-32\lib\site-packages\pandas\util\testing.py)
