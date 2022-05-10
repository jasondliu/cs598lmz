import gc, weakref, os
from collections import defaultdict

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.pipeline import _name_estimators
from sklearn.utils.metaestimators import _BaseComposition
from sklearn.utils.deprecation import _deprecate_positional_args
from sklearn.utils.validation import check_memory
from sklearn.exceptions import NotFittedError
from sklearn.utils.fixes import _object_dtype_isnan

from .utils import (
    _check_input_dtype,
    _check_estimator,
    _check_target_dtype,
    _check_n_features,
    _check_feature_names,
    _repr_html_,
    _repr_markdown_,
)
from .utils import _check_input_dtype, _check_target_dtype
from .utils import _check_estimator, _
