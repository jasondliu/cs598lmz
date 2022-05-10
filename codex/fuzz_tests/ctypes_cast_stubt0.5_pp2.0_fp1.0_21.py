import ctypes
ctypes.cast(x, ctypes.py_object).value

# а потом преобразовать к нужному объекту

import numpy as np
np.asarray(x)

# Также можно преобразовать данные сразу в массив

x = np.array(x, dtype=np.float64)

# Возможно, придется преобразовать массив из одного типа в другой

x = x.astype(np.int64)

# Возможно, придется из
