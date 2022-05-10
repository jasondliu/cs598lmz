from _struct import Struct
s = Struct.__new__(Struct)
s.__init__ = lambda *a, **k: None
s.__setattr__ = lambda *a, **k: None
s.__getattribute__ = lambda *a: None
s.__delattr__ = lambda *a: None

import sys
sys.modules['_struct'] = s
import numpy
sys.modules['_struct'] = Struct
import numpy.core._dotblas

import numpy.core.multiarray
import numpy.core.umath
import numpy.core.umath_tests
import numpy.core.fromnumeric
import numpy.core.defmatrix
import numpy.core.numeric
import numpy.core.numerictypes
