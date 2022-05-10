import ctypes
ctypes.CDLL("./libletwarp.so")

from pywarp import warping

def my_inverse_vector_field_wrap(size, U, V, Vx, Vy, Vz):
    warping.inverse_vector_field(size, U, V, Vx, Vy, Vz)
    
def my_vector_field_wrap(size, U, V, Vx, Vy, Vz):
    warping.vector_field(size, U, V, Vx, Vy, Vz)
