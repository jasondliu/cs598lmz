import weakref

from nengo.base import Process, NengoObject
from nengo.utils.compat import is_number, range, iteritems
from nengo.utils.stdlib import Timer


class Probeable(object):
    """Base class for objects that can be probed.

    Parameters
    ----------
    label : str, optional
        A descriptive label for this object.
    seed : int, optional
        The seed used for random number generation.
    add_to_container : bool, optional
        Whether this network will be added to a container.
        If readonly is True, this must be False.
    """

    def __init__(self, label=None, seed=None, add_to_container=None):
        self.label = label
        self.seed = seed
        self.add_to_container = add_to_container
        self.probes = {}

    def probe(self, target, probe_obj=None, sample_every=None):
        """Return a Probe object that probes the given target on this object.

        Parameters
        ----------
       
