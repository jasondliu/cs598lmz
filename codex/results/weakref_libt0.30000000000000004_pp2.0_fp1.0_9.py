import weakref

from . import _base
from . import _compat
from . import _util
from . import _util_py2
from . import _util_py3
from . import _util_py33
from . import _util_py34
from . import _util_py35
from . import _util_py36
from . import _util_py37
from . import _util_py38
from . import _util_py39


__all__ = [
    'Mock',
    'MagicMock',
    'NonCallableMock',
    'NonCallableMagicMock',
    'DEFAULT',
    'call',
    'create_autospec',
    'ANY',
    'sentinel',
    'mock_open',
    'PropertyMock',
    'patch',
    'patch.object',
    'patch.multiple',
    'patch.dict',
    'patch.stopall',
    'sentinel',
    'DEFAULT',
    'FILTER_DIR',
    'mock_open',
    'PropertyMock',
