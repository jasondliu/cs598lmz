import gc, weakref
from sklearn.base import BaseEstimator, TransformerMixin

from .utils import _get_all_features
from .features import _get_numeric_features, _get_categorical_features
from .features import _get_datetime_features

from ._transformers_utils import _get_columns_to_drop, _get_columns_to_fit
from ._transformers_utils import _get_columns_to_fit_and_transform, _get_columns_to_transform

# =============================================================================
# Base transformers
# =============================================================================

class BaseTransformer(BaseEstimator, TransformerMixin):
    """Base class for all transformers in Auto-TS.

    Parameters
    ----------
    columns_to_drop : list of str, default=None
        Columns to drop.

    columns_to_fit : list of str, default=None
        Columns to fit.

    columns_to_fit_and_transform : list of str, default=None
        Columns to fit and transform.

    columns_to_transform : list of str
