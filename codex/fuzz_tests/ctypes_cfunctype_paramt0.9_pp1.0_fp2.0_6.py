import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_double )

# this defn of factorial shadows the factorial fn imported from numpy
# and hence numpy.factorial will return always 52
def factorial( n_or_k ):
    if n_or_k == 0:
        return 1
    return n_or_k * factorial( n_or_k - 1 )

# this defn of power causes a warning in NumPy
def power( base, exp ):
    return base**exp

class MyStats( object ):
    def __init__( self, **kwargs ):
        if 'n' in kwargs:
            self.n = kwargs['n']
        if 'variance' in kwargs:
            self.variance = kwargs['variance']

    def __str__(self):
        return "vars:\nn = %f\nvariance = %f\n" % ( self.n, self.variance )

    def __repr__(self):
        return "vars:\nn = %f\nvariance
