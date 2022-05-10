import socket
import sys
import time

from raptiformica.actions.mesh import wait_for_mesh_to_form
from raptiformica.actions.mesh import wait_for_machines_to_check_in
from raptiformica.utils import retry
from tests.testcase import TestCase


class TestWaitForMeshToForm(TestCase):
    def setUp(self):
        self.set_env_vars()

        self.time = time
        self.retry = self.patch('raptiformica.utils.retry')
        self.retry.side_effect = lambda *args, **kwargs: args[0]
        self.wait_for_machines_to_check_in = self.patch(
            'raptiformica.actions.mesh.wait_for_machines_to_check_in'
        )

        self.start_time = time.time()
        self.timeout = 30
        self.expected_machine_type = 'headless'

    def test_wait_for_mesh_to_form_
