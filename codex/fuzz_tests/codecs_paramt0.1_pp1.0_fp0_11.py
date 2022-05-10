import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, exists

from os \
    import makedirs

from sys \
    import argv

from glob \
    import glob

from re \
    import compile

from codecs \
    import open

from optparse \
    import OptionParser

from cPickle \
    import load, dump

from numpy \
    import array, zeros, ones, concatenate, dot, transpose, outer, sqrt, \
           sum, mean, std, arange, argmin, argmax, argsort, newaxis, \
           searchsorted, where, loadtxt, savetxt, save, load

from numpy.random \
    import rand, randn, seed

from scipy.stats \
    import norm, pearsonr

from scipy.linalg \
    import svd, pinv

from scipy.sparse \
    import csr_
