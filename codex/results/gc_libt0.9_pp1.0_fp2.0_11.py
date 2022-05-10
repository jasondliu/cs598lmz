import gc, weakref
import textwrap, struct

from IPython.utils.process import arg_split
import IPython.testing.decorators as dec
from IPython.testing import tools as tt, decorators as dec

from .clusterdir import ClusterDir
import IPython.parallel as parallel
from IPython.parallel import spread


class MockHub(object):
    """Mock hub object for testing purposes.

    Use this so that the tasks to be executed by the controller, MBView
    instance, etc. do not attempt to access a hub object, instead we just
    pass in None.
    """
    def __init__(self, profile, cluster_id):
        self._profile = profile
        self._cluster_id = cluster_id
        self.client = MagicMock()

    @property
    def cluster_id(self):
        return self._cluster_id

    @property
    def profile(self):
        return self._profile

    def get_controller(self):
        return self.client


class MockKernel(MagicMock):
    """Mock kernel instance for
