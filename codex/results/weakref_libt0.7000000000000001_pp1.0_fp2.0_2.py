import weakref
from IPython.utils.traitlets import (
    HasTraits, Instance, Dict, List, Int, Enum, Bool, Str, Float, Bytes, Any,
    observe, default
)
from jupyter_client import BlockingKernelClient
from tornado.ioloop import IOLoop
from tornado import gen
from .protocol import KernelInfoReply, KernelOutput
from .decorators import synchronized

logger = logging.getLogger(__name__)


class KernelManager(HasTraits):
    """Manages a single kernel in a subprocess on this host.

    This version starts kernels with Popen.
    """

    kernel_manager_factory = Instance('jupyter_client.KernelManager')
    client = Instance('jupyter_client.BlockingKernelClient')

    def __init__(self, **kwargs):
        super(KernelManager, self).__init__(**kwargs)
        self.client = BlockingKernelClient()

    def start_kernel(self, **kwargs):
        k
