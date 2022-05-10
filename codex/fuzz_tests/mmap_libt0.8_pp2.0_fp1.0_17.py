import mmap
import errno

from cme import common
from cme.common import CMEModule


class Module(CMEModule):

    def __init__(self, **kwargs):
        super(Module, self).__init__(**kwargs)
        self.creds = []

    def enumerate_tasks(self):
        for server in self.servers:
            for host in self.get_hosts(server):
                if not host.is_windows() or not host.has_powershell():
                    continue

                yield host

    def read_file(self, remote_path, host):
        try:
            with self.read_file_from_host(remote_path, host) as rf:
                mm = mmap.mmap(rf.fileno(), 0, access=mmap.ACCESS_READ)

                while True:
                    line = mm.readline()

                    if not line:
                        break

                    line = line.decode('utf-16')
                    username = None
                    password = None

                    try:
                        user = re
