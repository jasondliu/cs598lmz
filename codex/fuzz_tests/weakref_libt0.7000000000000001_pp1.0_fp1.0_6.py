import weakref

import numpy as np

from . import dataset
from . import dataset_cache
from .. import utils
from .. import logging as logg
from .. import settings
from ..settings import verbosity


def preprocess(
    adata,
    filter_min_counts=True,
    filter_min_cells=True,
    filter_genes=None,
    min_counts=None,
    min_counts_u=None,
    min_counts_m=None,
    min_cells=None,
    max_counts=None,
    max_counts_u=None,
    max_counts_m=None,
    max_cells=None,
    n_top_genes=None,
    copy=False,
    layer=None,
    inplace=False,  # TODO: remove in 0.10.0
):
    """\
    Preprocess anndata object.

    Filter genes and cells based on counts, and normalize and log-transform the
    data.

    Parameters
    ----------
    adata
