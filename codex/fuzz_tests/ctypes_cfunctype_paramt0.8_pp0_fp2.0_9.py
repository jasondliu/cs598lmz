import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
from ctypes import *

class RbPolynomial(object):
    """
    A polynomial in \(z\), of arbitrary degree. It is implemented as a list of coefficients,
    from the lower order terms to the higher order terms.
    """
    def __init__(self, *coeffs):
        """
        Constructor.
        :param coeffs: A list of the polynomial coefficients, ordered from low order to high order.
        :type coeffs: A list of double
        """
        self.coeffs = coeffs
        self.degree = len(coeffs) - 1
        self.eval = FUNTYPE(self._eval)

    def roots(self):
        """
        Finds the roots of the polynomial using the Jenkins-Traub method.
        :return: a list containing the roots of the polynomial
        """
        from .JenkinsTraub import Polynomial
        p = Polynomial(self.coeffs)
        p.polyroot()

