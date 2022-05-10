import selection_test
import sys
import time
import umockdev
import unittest


class MockSession(object):
    """Mock session class to simulate the session info."""

    def __init__(self, user_name, system_id):
        """Mock session values.

        @param user_name: user name.
        @param system_id: system id.
        """
        self.user_name = user_name
        self.system_id = system_id


class MockConsoleKit(object):
    """Mock implementation of ConsoleKit."""

    def get_session_for_sysfs(self, sysfs_path):
        """Mock implementation of get_session_for_sysfs.

        @param sysfs_path: The sysfs path of the session.
        """
