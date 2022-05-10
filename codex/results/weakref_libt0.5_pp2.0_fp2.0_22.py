import weakref
from numpy import array, asarray, ndarray, empty, empty_like, zeros, int8, float32
from numpy import dot, cross, transpose, vstack, hstack, sqrt, sum, all, any
from numpy.linalg import norm
from numpy.random import rand

from pyNastran.bdf.field_writer_8 import set_blank_if_default
from pyNastran.bdf.cards.base_card import BaseCard, expand_thru, collapse_thru
from pyNastran.bdf.bdf_interface.assign_type import (
    integer, integer_or_blank, double, double_or_blank,
    string, string_or_blank, blank, integer_or_string)
from pyNastran.bdf.field_writer_8 import print_card_8, print_float_8, print_int_card
from pyNastran.bdf.field_writer_16 import print_card_16, print_float_16, print_int_card_16
from pyNastran
