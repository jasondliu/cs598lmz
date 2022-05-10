import ctypes
ctypes.cdll.LoadLibrary('/usr/lib/libgsl.so')
ctypes.cdll.LoadLibrary('/usr/lib/libgslcblas.so')
import scipy.stats as ss
import scipy.special as ssp
import scipy.optimize as sopt
 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

