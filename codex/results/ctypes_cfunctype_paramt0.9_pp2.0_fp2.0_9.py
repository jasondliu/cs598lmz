import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def initialize_library(filepath) :
    global lib, createPoissonGraph, getMaxDegree, deletePoissonGraph
    lib = ctypes.cdll.LoadLibrary(filepath)
    createPoissonGraph = lib.createPoissonGraph
    createPoissonGraph.argtypes = (ctypes.c_uint, FUNTYPE)
    createPoissonGraph.restype = ctypes.c_void_p
    getMaxDegree = lib.getMaxDegree
    getMaxDegree.argtypes = (ctypes.c_void_p,)
    getMaxDegree.restype = ctypes.c_uint
    deletePoissonGraph = lib.deletePoissonGraph
    deletePoissonGraph.argtypes = (ctypes.c_void_p,)
    deletePoissonGraph.restype = None

# Call this function to make sure that the class is initialized correctly.
initialize_library("libpcdgenerator.so")

# Generate a Poisson random graph from the library.
class
