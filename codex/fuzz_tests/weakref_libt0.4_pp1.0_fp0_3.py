import weakref
from collections import OrderedDict
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
from scipy.optimize import minimize
from scipy.optimize.optimize import OptimizeResult
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted

from .base import BaseModel
from .utils import check_X_y, check_X_y_sample_weight
from .utils import check_array, check_array_1d, check_array_2d
from .utils import check_sample_weight, check_X_y_binary
from .utils import check_X_y_classification, check_X_y_regression
from .utils import check_X_y_sample_weight_regression
from .utils import check_X_y_sample_weight_classification
from .utils import check_X_y_sample_weight_binary
from .utils import check_X_y_sample_weight_multilabel
from .utils import check_X_y_sample_weight_mult
