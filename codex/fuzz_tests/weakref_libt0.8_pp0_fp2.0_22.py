import weakref
import sys
import os
import types

from threading import RLock

from gns3server.modules.dynamips import DEFAULT_DYNAMIPS_PORT, DEFAULT_DYNAMIPS_BASE_UDP_PORT, DEFAULT_WORKER_THREADS_POOL_SIZE, DEFAULT_HOST_WORKER_THREAD_TIMEOUT
from gns3server.modules.vpcs import DEFAULT_VPCS_PORT
from gns3server.modules.iou import DEFAULT_IOU_PORT

import logging
log = logging.getLogger(__name__)


class ServerConfig(ConfigObj):

    """
    Server configuration (loaded from a file).
    """

    def __init__(self, path):

        ConfigObj.__init__(self, infile=path, encoding="utf-8", create_empty=True, write_empty_values=True)
        self.path = path

        # version
        if "version" not in self:
            self["version"] = 1

        if self["version"] > 1:
           
