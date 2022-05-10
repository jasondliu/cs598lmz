import gc, weakref

import numpy as np

from sklearn.utils import check_random_state

from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_less
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_false
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import ignore_warnings

from sklearn.externals.joblib import Parallel, delayed

from sklearn.base import clone

from sklearn.utils import check_random_state

import sklearn.utils.estimator_checks as estimator_checks

from sklearn.datasets import load_iris
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import SGDRegressor
from sklearn.
