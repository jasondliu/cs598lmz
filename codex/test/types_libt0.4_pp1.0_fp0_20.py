import types
types.ModuleType.__getattr__ = lambda self, name: self.__dict__[name]

import sys
sys.path.append("../../../../")

from mupif import *
import Pyro4
import logging
log = logging.getLogger()
import time as timeTime
import mupif.Physics.PhysicalQuantities as PQ

nshost = '172.30.0.1'
nsport = 9090
hkey = 'mupif-secret-key'
digimatJobManName = 'eX_DigimatMF_JobManager'
digimatName = 'eX_DigimatMF'
vpsJobManName = 'VPS_JobManager'
vpsName = 'VPS'

testName = 'test_vps_digimat_thermal_stress'

#locate nameserver
ns = PyroUtil.connectNameServer (nshost, nsport, hkey)

#connect to JobManager running on (remote) server

#digimatJobMan = PyroUtil.connectJobManager (ns, dig
