import weakref
import traceback
import logging
import threading
from pytools.log import MultiHandler
from pytools.obj_array import flat_obj_array

from pyvolve import evolver, tree_reader, partition
from pyvolve import amino_acid_models as aa_model_module
from pyvolve import matrix_builder as mb
from pyvolve import model_builder as mdl_builder
from pyvolve import nucleotide_models as nt_model_module
from pyvolve import tree_utils
from pyvolve._tools import _resolve_names
from pyvolve.warnings import _warn_user


__author__ = "Martin Hunt"
__email__ = "mmh@pitt.edu"

_LOG_FORMAT = (
    "%(asctime)s %(levelname)s "
    + "%(name)s.%(module)s:%(funcName)s:%(lineno)d - %(message)s"
)

_LOGGER = logging.getLogger(__name__)


class TreeProcessor(object
