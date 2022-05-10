import socket
# Test socket.if_indextoname()
import sys
# Test sys.implementation
import termios


class _TestModule(object):
    _testcases = None  # Lazy-initialized list of test cases

    def __init__(self):
        pass

    def __iter__(self):
        if self._testcases is None:
            self._testcases = [
                getattr(self, attr) for attr in dir(self)
                if attr.startswith('test_')]
        return iter(self._testcases)


class TestLinuxModule(_TestModule):
    """Test that the module correctly identifies Linux"""
    def test_OS(self):
        assert sys.platform == 'linux'

    def test_version(self):
        assert 'linux' in sys.version.lower()

    def _test_posix(self):
        import posix
        assert posix.name == 'posix'
        assert posix.uname() == posix.uname

