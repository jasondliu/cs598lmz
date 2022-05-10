import weakref

import numpy as np

from . import Base
from . import _classes

from . import _getters
from . import _setters

from .. import _core
from .. import _dtypes

from .._filters import common_filter as com_f
from .._filters import rank_filter as rank_f
from .._filters import threshold_filter as th_f

from .._tierpsytools.read_data import get_valid_contour_area, get_valid_bob_area


class Features(Base):
    _name = 'features'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._features = {}
        self._features_cache = {}

        self._aux_columns = None

    def _check_features(self, columns):
        if isinstance(columns, str):
            columns = [columns]

