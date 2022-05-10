import types
types.ClassType = type

from DIRAC import S_OK, S_ERROR
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC.Core.Utilities.ThreadPool import ThreadPool

from DIRAC.ResourceStatusSystem.DB.ResourceStatusDB import ResourceStatusDB
from DIRAC.ResourceStatusSystem.PolicySystem.PEP import PEP

import time

__RCSID__ = '$Id: $'

def initializeResourceStatusHandler( serviceInfo ):

  retVal = loadPolicies( serviceInfo )
  if not retVal[ 'OK' ]:
    return retVal

  return S_OK()

class ResourceStatusHandler( RequestHandler ):

#############################################################################

  def initialize( self ):

    self.rsDB = ResourceStatusDB()
    self.policies = {}

#############################################################################

