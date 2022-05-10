import weakref
import sys
import traceback
import threading

import pywbem
from pywbem import CIMError
from pywbem import CIM_ERR_NOT_SUPPORTED
from pywbem import CIM_ERR_INVALID_NAMESPACE
from pywbem import CIM_ERR_INVALID_PARAMETER
from pywbem import CIM_ERR_INVALID_CLASS
from pywbem import CIM_ERR_NOT_FOUND
from pywbem import CIM_ERR_INVALID_OPERATION
from pywbem import CIM_ERR_FAILED
from pywbem import CIM_ERR_CLASS_HAS_CHILDREN
from pywbem import CIM_ERR_CLASS_HAS_INSTANCES
from pywbem import CIM_ERR_INVALID_SUPERCLASS
from pywbem import CIM_ERR_ALREADY_EXISTS
from pywbem import CIM_ERR_NO_SUCH_PROPERTY
from pywbem import C
