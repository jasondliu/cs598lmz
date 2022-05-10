import weakref

import numpy as np

from . import utils
from . import constants
from . import objects
from . import events
from . import data
from . import features
from . import plotting
from . import clustering
from . import export
from . import visualization
from . import preprocessing
from . import external
from . import pipeline
from . import settings
from . import logging as logg
from . import _utils
from . import _settings
from . import _compat
from . import _version
from . import _doc


@_utils.deprecated('scanpy.api')
class AnnData(object):
    """\
    An annotated data matrix.

    :param adata:
        Annotated data matrix.
    :param X:
        `adata.X`: `adata.X` is a sparse or dense matrix of shape
        `n_obs × n_vars` `(n_cells × n_genes)` containing the data.
    :param obs:
        `adata.obs`: `adata.obs` is a `pandas.DataFrame` that holds

