import gc, weakref

import numpy as np

from sklearn.utils.fixes import signature, _object_dtype_isnan
from sklearn.utils.validation import _check_sample_weight
from sklearn.utils.multiclass import class_distribution
from sklearn.utils.multiclass import unique_labels
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.metaestimators import if_delegate_has_method
from sklearn.utils.optimize import newton_cg
from sklearn.utils.validation import check_array
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.validation import _deprecate_positional_args
from sklearn.utils.validation import DataConversionWarning
from sklearn.utils.extmath import softmax
from sklearn.exceptions import ConvergenceWarning
from sklearn.exceptions import NotFittedError
from sklearn.exceptions import ChangedBehaviorWarning
from sklearn
