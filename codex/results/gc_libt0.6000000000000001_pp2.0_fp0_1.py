import gc, weakref
from time import time

from numpy import (
    array, dot, zeros, empty,
    allclose, sqrt, linalg,
    ndarray, vstack, all,
    nan_to_num, asarray
)
from numpy.linalg import norm
from numpy.random import rand

from pyNastran.bdf.field_writer_8 import print_card_8
from pyNastran.bdf.field_writer_16 import print_card_16
from pyNastran.bdf.bdf_interface.assign_type import (
    integer, integer_or_blank, double, double_or_blank,
    string, string_or_blank,
)
from pyNastran.bdf.dev_vectorized.cards.vectorized_card import VectorizedCard

from pyNastran.bdf.dev_vectorized.utils import slice_to_iter
from pyNastran.bdf.field_writer_8 import set_blank_if_default
from pyNastran.bdf.cards.base_
