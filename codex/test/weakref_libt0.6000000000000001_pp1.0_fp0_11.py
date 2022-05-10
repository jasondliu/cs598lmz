import weakref
import logging

from pkg_resources import resource_filename

from numpy import (
    linspace, logspace, log10,
    array, zeros, ones,
    sparse, where, isnan, nan,
    vstack, hstack,
    argsort,
    dot, asarray,
    ascontiguousarray,
    empty,
    ndarray,
)

from numpy.linalg import norm

from scipy.linalg import (
    eig,
    inv,
    solve,
    pinv,
    LinAlgError,
)

from scipy.sparse import (
    csr_matrix,
    vstack as spvstack,
    hstack as sphstack,
)

from scipy.sparse.linalg import (
    spsolve,
    norm as spnorm,
    splu,
    eigsh,
)

from scipy.optimize import (
    newton,
    brentq,
)

from . import utils
