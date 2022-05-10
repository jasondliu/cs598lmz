import weakref
import logging

from numpy import array, zeros, ones, arange, concatenate, searchsorted, \
                  where, unique, asarray, ndarray, empty, ascontiguousarray, \
                  dot, transpose, hstack, vstack, savetxt, loadtxt
from numpy.linalg import norm

from pyNastran.bdf.fieldWriter import print_card_8
from pyNastran.bdf.fieldWriter16 import print_card_16
from pyNastran.bdf.bdfInterface.assign_type import (integer, integer_or_blank,
    double_or_blank, integer_double_or_blank, string_or_blank)

from pyNastran.bdf.dev_vectorized.cards.vectorized_card import VectorizedCard

from pyNastran.bdf.cards.baseCard import (BaseCard, expand_thru,
                                          collapse_thru_by, _node_ids)
from pyNastran.bdf.cards.collpase_card import collapse_thru_
