import gc, weakref
import numpy as np
import scipy.sparse as sp
from . import glm_fit
from .utils import (
    check_array, check_random_state, check_X_y, check_consistent_length, check_array_length_equal)
from .utils.validation import check_is_fitted
from .utils.extmath import safe_sparse_dot, row_norms
from .utils.multiclass import check_classification_targets
from .utils.validation import _num_samples, column_or_1d
from .utils.fixes import sparse_lsqr
from .utils.stats import _weighted_percentile
from .utils.validation import has_fit_parameter, check_X_y
from .exceptions import ConvergenceWarning
from .linear_model.base import LinearModel
from .base import BaseEstimator, RegressorMixin, ClassifierMixin


class BaseSGD(BaseEstimator):
    """Base class for SGD classification and regression."""

    def __init__(self, loss, penalty='l
