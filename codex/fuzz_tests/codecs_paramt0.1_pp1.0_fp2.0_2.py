import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath, exists

from os \
    import makedirs

from sys \
    import argv, exit

from optparse \
    import OptionParser

from cPickle \
    import dump, load

from time \
    import time

from numpy \
    import array, zeros, ones, empty, arange, concatenate, \
           where, argsort, searchsorted, unique, hstack, vstack, \
           newaxis, savetxt, loadtxt, save, load, savez, load as nload

from numpy.random \
    import seed, randint, rand, randn, permutation

from scipy.sparse \
    import csr_matrix, lil_matrix, coo_matrix, issparse

from scipy.sparse.linalg \
    import spsolve

from scipy.linalg \

