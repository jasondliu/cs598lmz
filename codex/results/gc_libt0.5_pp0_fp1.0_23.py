import gc, weakref
import numpy as np
import dask.array as da
from dask.array.core import _maybe_wrap_in_dask_array, _maybe_unwrap_dask_array
from dask.array.utils import assert_eq, same_keys
from dask.array.routines import broadcast_to, reshape, transpose, concatenate
from dask.base import compute, normalize_token, tokenize, _token_key, compute_as_if_collection
from dask.highlevelgraph import HighLevelGraph
from dask.blockwise import Blockwise
from dask.utils import is_dask_collection, is_arraylike, is_collections, is_list_like
from dask.utils_test import inc
from dask.array.core import Array
import pytest
from toolz import concat, first, take, merge
from operator import getitem
from dask.array.chunk import Tuple, Chunk
from dask.array.rechunk import rechunk
from dask.array.core import getem
from dask.array.
