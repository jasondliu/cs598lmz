import bz2
bz2c = bz2.compress
bz2u = bz2.decompress
bz2f = bz2.BZ2File

import cStringIO
cStringIOc = cStringIO.StringIO.write
cStringIOu = cStringIO.StringIO
cStringIOf = cStringIO.StringIO.write

import cPickle
cPicklec = cPickle.dumps
cPickleu = cPickle.loads

import util
utilc = util.compress
utilu = util.decompress
utilf = None

codecs = {'bz2':(bz2c, bz2u, bz2f),
    'cstringio':(cStringIOc, cStringIOu, cStringIOf),
    'c':(cPicklec, cPickleu, None),
    'util':(utilc, utilu, utilf),
    }

fileprotocol = 'persistent'
#fileprotocol = 'transient'
#fileprotocol = 'temporary'
#
