import gc, weakref
import cPickle as pickle

from numpy import atleast_1d, sort, unique, reshape, take, \
     asarray, iscomplexobj, issubdtype, array, zeros, \
     int8, int32, float64, integer, empty, newaxis, \
     ndarray, result_type, add, multiply, \
     nonzero, maximum, minimum, dot, alltrue, transpose, \
     compress, indices, where, arange, zeros_like

from numpy.linalg import eigvals
from numpy.random import permutation

from scipy.sparse import isspmatrix, isspmatrix_csr, \
     isspmatrix_bsr, isspmatrix_csc, isspmatrix_coo, \
     isspmatrix_lil, isspmatrix_dok, coo_matrix, \
     spmatrix, csc_matrix, bsr_matrix, csr_matrix, lil_matrix, dok_matrix, \
     h
