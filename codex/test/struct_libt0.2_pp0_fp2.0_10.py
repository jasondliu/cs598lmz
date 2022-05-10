import _struct

from . import _common
from . import _compat
from . import _errors
from . import _util
from . import _vendor
from . import _winreg

_logger = _util.get_logger(__name__)

_DEFAULT_REGISTRY_PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'

_REGISTRY_PATH_ENV_VAR = 'PIP_FIND_LINKS_REGISTRY_PATH'

_REGISTRY_PATH_ENV_VAR_DEFAULT = 'PIP_FIND_LINKS_REGISTRY_PATH_DEFAULT'

_REGISTRY_PATH_ENV_VAR_DEFAULT_VALUE = _DEFAULT_REGISTRY_PATH

_REGISTRY_PATH_ENV_VAR_DEFAULT_VALUE_OLD = r'SOFTWARE\Python\PythonCore'

_REGISTRY_PATH_ENV_VAR_DEFAULT_VALUE_OLD_2 = r'SOFTWARE\Python\PythonCore\2.7'
