import codecs
# Test codecs.register_error
def hex_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [ "\\x%02x" % ord(c) for c in exc.object[exc.start:exc.end] ]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("can't handle %.400s" % exc)
codecs.register_error("hex_replace", hex_replace)

import sys
sys.path.append("../")
import cnn_rnn
import lib.layers as layers

from scipy.sparse import lil_matrix
from sklearn.preprocessing import normalize


def readfile(filename):
  # return a base filename
  # if 'cnn-rnn' not in filename:
  #   return ''.join(filename.split('/')[-1].split('_')[:-1])
  # else:
  #   return 'cnn-rnn'
  filename = filename.split('/')[-1]
  if filename.endswith(
