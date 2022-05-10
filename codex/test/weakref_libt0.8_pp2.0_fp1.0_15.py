import weakref, copy
from . import types, parameter
from .parameter import Parameter
from .types import AnyType, ListType, DictType, IntType, FloatType, \
    BoolType, StrType, FunctionType, OptionalType, EnumType
from . import serialize

log = logging.getLogger(__name__)

class ConfigTypeError(TypeError): pass

class ConfigValueError(ValueError): pass

class ConfigPathError(ValueError): pass

class ConfigMissingError(ConfigValueError): pass

class ConfigIncompatibleTypes(ConfigValueError): pass

class ConfigIncompatibleValue(ConfigValueError): pass

class ConfigIncompatibleParameter(ConfigValueError):

    def __init__(self, parameter, value, path=None):
        message = ("%r is not compatible with parameter '%s'" %
                   (value, parameter.name))
        if path is not None:
            message += " at " + path
        super(ConfigValueError, self).__init__(message)

