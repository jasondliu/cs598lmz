import weakref
from pkg_resources import resource_filename
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions

from .. import __version__
from .. import _sage_const_log as log
from ..util import json
from ..util.misc import SageCellVersion
from ..util.temporary_file import atomic_write
from ..util.decorators import sage_wraps, skip_doctest
