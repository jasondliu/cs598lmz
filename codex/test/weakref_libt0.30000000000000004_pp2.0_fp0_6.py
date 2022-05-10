import weakref

from . import _common
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

_util.patch_collections_abc()

_util.patch_functools_wraps()

_util.patch_types_mro()

_util.patch_types_new_class()

_util.patch_types_with_metaclass()

_util.patch_typing_get_args()

_util.patch_typing_get_origin()

_util.patch_typing_get_parameters()

_util.patch_typing_get_type_hints()

_util.patch_typing_io()

_util.patch_typing_type_check()


