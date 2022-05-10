import ctypes
ctypes.cast(None, ctypes.py_object)
from ctypes.util import find_library

from docutils import nodes
from docutils import utils
from docutils.parsers.rst import roles
from docutils.statemachine import ViewList

from sphinx.util import get_doc_object_name
from sphinx.util import logging
from sphinx.util.nodes import make_refnode


logger = logging.getLogger(__name__)


class MocException(Exception):
    pass


def _find_libmoc():
    """Find libmoc."""
    libmoc = None

    # check if it is in the default path
    libmoc_path = find_library("moc")

    # if it is not in the default path
    if libmoc_path is None:
        # check if it is in the python build directory
        python_build_prefix = os.path.dirname(
            sysconfig.get_config_var("LIBDIR"))
        libmoc_path = os.path.join(python_
