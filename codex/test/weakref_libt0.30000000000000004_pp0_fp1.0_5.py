import weakref

from . import _common
from . import _compat
from . import _util
from . import _vendor
from . import _vendor_packages
from . import _vendor_spec

_logger = _compat.logging.getLogger(__name__)

_DEFAULT_INDEX_URL = 'https://pypi.python.org/simple'

_PIP_VERSION = _vendor_packages.parse_version('pip==18.1')

_PIP_VERSION_REQUIREMENT = _vendor_spec.SpecifierSet('pip==18.1')

_PIP_VERSION_SPECIFIER = _vendor_spec.SpecifierSet('pip==18.1')

_PIP_VERSION_SPECIFIER_REQUIREMENT = _vendor_spec.SpecifierSet('pip==18.1')

_PIP_VERSION_SPECIFIER_REQUIREMENT_REQUIREMENT = _vendor_spec.SpecifierSet('pip==18.1')

_PIP_VERSION_SPECIFIER_
