import select
import subprocess

from . import BaseDevice, get_adb_path, get_adb_device_arg
from .. import exceptions
from ..utils import get_free_tcp_port


class AndroidDevice(BaseDevice):
    """Android device implementation."""

    _logcat = None
    _use_mdev = False
    _mdev_dir = None
    _mdev_files = []
    _mdev_env = None
    _mdev_proc = None

    def __init__(self, adb_server_host=None, adb_server_port=None,
                 device_serial=None, logger=None, **kwargs):

        super(AndroidDevice, self).__init__(logger=logger, **kwargs)

        self.adb_server_host = adb_server_host
        self.adb_server_port = adb_server_port
        self.device_serial = device_serial
        self.popen_adb_list_proc = None
        self._logcat = None

        self.connect_to
