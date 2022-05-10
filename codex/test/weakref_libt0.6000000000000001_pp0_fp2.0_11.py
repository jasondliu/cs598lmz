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
