import sys, threading
threading.Thread(target=lambda: sys.exit()).start() 
from TrigCostPython import TrigCostAnalysis
from TrigCostPython import TrigCostCool
import unittest

from AthenaCommon.Configurable import Configurable
Configurable.configurableRun3Behavior = True

from AthenaCommon.AlgSequence import AlgSequence

from AthenaCommon.Logging import logging
from AthenaCommon.Constants import *
from AthenaCommon.AppMgr import ServiceMgr as svcMgr
from AthenaCommon.AppMgr import theApp

from AthenaCommon.DetFlags import DetFlags

from AthenaCommon.GlobalFlags import globalflags
from AthenaCommon.JobProperties import jobproperties
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags

from AthenaPoolCnvSvc.PoolReadConfig import PoolReadCnvSvc
from AthenaPoolCnvSvc.PoolReadConfig import PoolReadCfg
from AthenaPoolCnvSvc.PoolReadConfig import PoolFileList

from AthenaCommon.AppMgr import ToolSvc

from PyJobTransformsCore.runargs import RunArguments
