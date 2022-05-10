import weakref

import numpy as np

from scipy.sparse.csgraph import connected_components

from dolo.numeric.serial_operations import serial_multiplication
from dolo.numeric.serial_operations import serial_inversion
from dolo.numeric.serial_operations import serial_solve
from dolo.numeric.serial_operations import serial_cholesky
from dolo.numeric.serial_operations import serial_eigenvalues
from dolo.numeric.serial_operations import serial_eigenvectors
from dolo.numeric.serial_operations import serial_inverse_cholesky
from dolo.numeric.serial_operations import serial_inverse_cholesky_solve
from dolo.numeric.serial_operations import serial_inverse_cholesky_inversion
from dolo.numeric.serial_operations import serial_transpose
from dolo.numeric.serial_operations import serial_kron
from dolo.numeric.serial_operations import serial_dot
