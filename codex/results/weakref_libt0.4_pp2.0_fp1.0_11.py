import weakref

import numpy as np
from numpy.testing import assert_equal, assert_almost_equal

from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_false
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_warns
from sklearn.utils.testing import ignore_warnings
from sklearn.utils.testing import assert_raise_message
from sklearn.utils.testing import assert_no_warnings

from sklearn.utils import check_random_state
from sklearn.utils import safe_mask
from sklearn.utils import safe_indexing
from sklearn.utils import shuffle
from sklearn.utils import gen_batches
from sklearn.utils import gen_even_slices
from sklearn.utils import resample
from sklearn.utils import check_array
from sklearn.utils import column_or_1d
from sklearn.utils import check_consistent_length
from sklearn.utils import check_X_y

