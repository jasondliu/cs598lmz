import gc, weakref
from gsl_utilities import *

from gsl_matrix import Matrix
from gsl_vector import Vector

__all__ = ['Covariance']

_cov_gsl_types = {
    'float': gsl.GSL_TYPE_FLOAT,
    'double': gsl.GSL_TYPE_DOUBLE,
    'longdouble': gsl.GSL_TYPE_LONG_DOUBLE
}

_cov_gsl_types_inverse = dict([(v, k) for k, v in _cov_gsl_types.items()])

class Covariance(object):
    """docstring for Covariance"""
    def __init__(self, data=None, dim=None, gsl_type=None):
        super(Covariance, self).__init__()
        self.data = None
        self.dim = None
        self.gsl_type = None
        self.__gsl_type = None
        self.__gsl_type_name = None
        self.
