import select
import socket
import sys
import threading

from casperfpga.utils import get_fpga_instances, normalise_host
from corr2 import utils


class Snapctl:
    def __init__(self, host, make_logger=False):
        self.logger = utils.make_logger(__name__, host
                                        if host is not None else 'localhost',
                                        make_logger)
        self.host = normalise_host(host)
        self.port_num = 8888
        self.fpga = get_fpga_instances(self.logger)[self.host]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(0)
        self.sock.connect_ex((self.host, self.port_num))
        self.lock = threading.Lock()

    def __enter__(self):
        return self

