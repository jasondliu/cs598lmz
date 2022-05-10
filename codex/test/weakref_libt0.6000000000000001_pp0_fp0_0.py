import weakref

import numpy as np
import pandas as pd

from .utils import _get_mask_bounds, _get_top_n_per_group
from .core import _Series, _Frame


class _GroupByMixin(object):
    """
    Implements type specific aggregation methods
    """

    def _get_numeric_data(self):
        """
        Return only numeric data
        """
        if isinstance(self._selected_obj, _Series):
            return self._selected_obj.copy()
        elif isinstance(self._selected_obj, _Frame):
            return self._selected_obj._get_numeric_data()
        else:  # pragma: no cover
            raise TypeError('invalid type: {typ}'.format(typ=type(self._selected_obj)))

    def _cython_agg_general(self, how, numeric_only=True):
        """
        Wrapper for cython agg
        """
