import gc, weakref
from pymel.internal.pmcmds import createNode, dR_createNode
from pymel.internal.pmutil import stripLeadingDollarSign
from pymel.internal.pmutil import postfixToCmdName, removeDupes
from pymel.internal.pmutil import getAsPyNodes, iterParentContexts
from pymel.internal.pmutil import getPyNodesFromPmNodeList
from pymel.internal.pmutil import getProgArgs

from random import randint
import sys
from pymel.internal.startup import mayaStartUpHasRun
from pymel.util import CmdFile
from pymel.util import getLogger
from pymel.internal.cmdcache import getCmdCache
from pymel.internal.cmdcache import numCmdsInCache, getNumCacheFiles
from pymel.internal.cmdcache import getCmdFilePath
from pymel.internal.cmdcache import cmdCacheWriteClash
from pymel.internal.cmdcache import cmdCacheWriteClash, getNumCmdsInCache
from p
