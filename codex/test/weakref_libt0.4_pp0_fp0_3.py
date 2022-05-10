import weakref

from . import _compat as _
from . import _compat
from . import _common
from . import _exceptions
from . import _impl
from . import _sqlalchemy_exceptions
from . import _util
from . import exc
from . import logging
from . import util
from . import util as sqlalchemy_util


_camelize_re = re.compile(r"(?:^|_)(.)")


def camelize(s):
    return _camelize_re.sub(lambda m: m.group(1).upper(), s)


def _camel_and_upper(name):
    return camelize(name).upper()


def _is_mapped_class(cls):
    return hasattr(cls, "__table__")


def _is_aliased_class(cls):
    return hasattr(cls, "__table__") and hasattr(cls, "__mapper__")


