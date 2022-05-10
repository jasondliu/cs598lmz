import weakref

from scipy import signal

from . import core
from . import operations
from . import signals
from . import optimization
from . import histogram


def _make_name(name, prefix):
    """Create a unique name for a signal.

    :param name: the base name
    :type name: str
    :param prefix: the prefix
    :type prefix: str
    """
    return '{}{}'.format(prefix, name)


class BinnedFit(object):
    """A class which holds information about a fit to a set of bins.

    :param bins: the bins used during the fit
    :type bins: list
    :param signal: the signal used during the fit
    :type signal: :class:`~pyhf.signals.Spectra`
    :param fit_results: the results of the fit
    :type fit_results: :class:`~pyhf.optimization.MinuitFitResults`
    """

    def __init__(self, bins, signal, fit_results):
        self._bins = bins
        self._sign
