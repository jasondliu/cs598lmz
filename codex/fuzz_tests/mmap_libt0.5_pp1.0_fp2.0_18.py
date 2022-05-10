import mmap
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from sklearn.utils import murmurhash3_32
from sklearn.utils.fixes import bincount
from sklearn.utils.validation import check_array

from .base import BaseEstimator, TransformerMixin
from .utils.validation import check_is_fitted


class FeatureHasher(BaseEstimator, TransformerMixin):
    """Convert a collection of text or categorical features to a
    numerical vector space, using a hashing trick.

    This transformer turns lists of text or categorical features into
    scipy.sparse matrices, using a hash function to compute the matrix
    column corresponding to each feature.

    By default, the output matrix type is sparse.csc_matrix. You can
    choose the output matrix type (e.g. dense numpy.ndarray) by
    setting the `dtype` parameter.

    Read more in the :ref:`User Guide <preprocessing_transformer>`.

    .. versionadded:: 0.20

   
