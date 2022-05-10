import mmap
# Test mmap.mmap()
import socket
# Test socket.socketpair()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.executable
import time
# Test time.time()
import traceback
# Test traceback.print_exc()


class Test(unittest.TestCase):
    def test_get_domain_name(self):
        self.assertEqual(machinename.get_domain_name(),
                         machinename.gethostbyname(socket.gethostname()).split('.')[1])
        self.assertEqual(machinename.get_domain_name(),
                         machinename.gethostbyname(socket.gethostname()).split('.')[1])

    def test_load_file(self):
        self.assertIsNotNone(machinename.load_file())

    def test_save_file(self):
        self.assertIsNone(machinename.save_file({'test': 'abc'}))

    def test_get_machine_name(self):
        self.assertEqual
