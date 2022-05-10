import codecs
# Test codecs.register_error('my_escape_encode', codecs.escape_encode)
import sys
# sys.stdout = sys.stderr
sys.path.append('../utils')
from myutils import vwap
from mytable import Mytable
from mystrategy import Mystrategy
from mymarketdata import Mymarketdata

########################################################################
# empty log file
open('arb.log', 'w').close()# creates the file

########################################################################
# load vwap strategy
with open('../bin/strategy/strategy.txt') as fp:
    vw_strategy = ast.literal_eval(fp.read())

########################################################################
vw = vwap()
# print(vw_strategy)
# print(vw.update(vw_strategy))
vw.update(vw_strategy)
########################################################################
# Load keys and other configuration
#with open('../bin/keys.txt') as fp:
with open('../bin/config.txt') as fp:
    config = ast.literal_eval(fp.
