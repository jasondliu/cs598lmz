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

from optparse \
    import OptionParser

from cPickle \
    import load, dump

from time \
    import time

from numpy \
    import array, zeros, ones, arange, array_equal, \
           concatenate, where, newaxis, transpose, \
           dot, sqrt, log, exp, sum, mean, std, \
           cov, corrcoef, vstack, hstack, savetxt, \
           loadtxt, save, load, savez, load as npload, \
           load as npload, save as npsave, savez as npsavez, \
           load as nploadz, save as npsavez, savez as npsavez, \
           load as
