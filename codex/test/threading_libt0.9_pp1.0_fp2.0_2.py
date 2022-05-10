import threading
threading.stack_size(2**25)

from fwk import common,fwk 
from fwk.mng import *

#==================================================================
# logging
#
COMMON = common.Common()
LOGGER = log.GetLogger(COMMON, COMMON.Logfile)
