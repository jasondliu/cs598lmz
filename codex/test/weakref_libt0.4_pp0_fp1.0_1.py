import weakref

import numpy as np
import scipy.sparse as sp

from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_array_almost_equal
from sklearn.utils.testing import assert_almost_equal
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_raise_message
from sklearn.utils.testing import assert_warns

from sklearn.base import clone
from sklearn.base import BaseEstimator
from sklearn.base import RegressorMixin
from sklearn.base import ClassifierMixin
from sklearn.base import TransformerMixin
from sklearn.base import is_classifier
from sklearn.base import is_regressor
from sklearn.base import is_transformer
from sklearn.base import MetaEstimatorMixin
from sklearn.base import is_outlier_detector
from sklearn.base import OutlierMixin
