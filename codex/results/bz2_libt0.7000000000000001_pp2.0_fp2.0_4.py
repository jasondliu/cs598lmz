import bz2
bz2.decompress(bz2_data)

import chardet
chardet.detect('hello world')

#import common

import cPickle
cPickle.loads(cPickle_data)

import cStringIO
cStringIO.StringIO(cStringIO_data)

import distutils.archive_util
distutils.archive_util.make_zipfile(None, None)

import gzip
gzip.open(gzip_data)

import StringIO
StringIO.StringIO(StringIO_data)

import zlib
zlib.decompress(zlib_data)
