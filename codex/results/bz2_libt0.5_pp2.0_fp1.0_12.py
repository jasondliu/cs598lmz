import bz2
bz2.test()

import zlib
zlib.test()

import zipfile
zipfile.test()

import gzip
gzip.test()

import tarfile
tarfile.test()

import cPickle
cPickle.test()

import cStringIO
cStringIO.test()

import csv
csv.test()

import doctest
doctest.testmod()

import locale
locale.setlocale(locale.LC_ALL, '')
locale.test()

import pdb
pdb.test()

import unittest
unittest.main(verbosity=2)

import pydoc
pydoc.test()

import distutils.tests
distutils.tests.test_suite()

import doctest
doctest.testmod()

import test
test.test_support.run_unittest(
    test.regrtest.REGRTEST_OPTIONS,
    test.test_support,
    test.test_warnings,
    test.test_grammar
