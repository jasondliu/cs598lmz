import gc, weakref
import types
import itertools

import nose
import numpy as np
from numpy.testing import (assert_, assert_equal, assert_raises,
                           assert_almost_equal, assert_allclose,
                           run_module_suite, dec, assert_array_equal,
                           assert_array_almost_equal, assert_array_less)

from scipy import signal
from scipy.signal import (lfilter, lfilter_zi, filtfilt, butter, cheby1,
                          cheby2, ellip, bessel, buttord, cheb1ord,
                          cheb2ord, ellipord, freqs, freqz, freqs_zpk,
                          group_delay, tf2zpk, zpk2tf, tf2sos, sos2tf,
                          sosfilt, sosfiltfilt, ss2tf, sos2ss, zpk2sos,
                          cont2discrete, lti, StateSpace, TransferFunction,
                          ZerosPoles
