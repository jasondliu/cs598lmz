import weakref

from . import _cim_xml
from .cim_constants import CIM_ERR_INVALID_CLASS, CIM_ERR_NOT_FOUND, CIM_ERR_INVALID_NAMESPACE
from .cim_obj import CIMClassName, CIMInstanceName, CIMParameter, \
    CIMProperty, CIMQualifier, CIMQualifierDeclaration, CIMMethod, CIMClass, \
    CIMInstance, CIMClassName, NocaseDict
from .tupleparse import tuple_to_cim_xml
from .errors import CIMXMLParseError, CIMError
from ._common import cimtype, _ensure_unicode
