import types
types.ModuleType.__new__ = __new__

import random
import pandas as pd
import numpy as np
import xarray as xr

from pysam import VariantFile

from t4_dask import _genotype_pool
from t4_dask import _variant_pool

from t4_dask import _get_contig
from t4_dask import _get_variant
from t4_dask import _get_variant_table
from t4_dask import _get_variant_table_columns

from t4_dask import _get_ref
from t4_dask import _get_alt
from t4_dask import _get_pos
from t4_dask import _get_id
from t4_dask import _get_qual
from t4_dask import _get_filter

from t4_dask import _get_info

from t4_dask import _get_format
from t4_dask import _get_genotype
from t4_dask import _get_genotype
