import types
types.ModuleType.__repr__ = lambda self: self.__name__

# We have to do this to avoid a circular import.
import numpy as np
from numpy.testing import (assert_allclose, assert_equal, assert_almost_equal,
                           assert_array_almost_equal, assert_array_equal)

from .. import (
    cdf,
    pdf,
    ppf,
    rvs,
    stats,
    _distn_infrastructure,
    _continuous_distns,
    _discrete_distns,
    _distn_names,
    _distn_doc_kwds,
    _distn_doc_default_callparams,
    _distn_doc_frozen_callparams,
    _distn_doc_frozen_callparams_ctor,
    _distn_doc_frozen_callparams_init,
    _distn_doc_frozen_callparams_init_doc,
    _distn_doc_frozen_callparams_init_doc_kwds,
    _distn_
