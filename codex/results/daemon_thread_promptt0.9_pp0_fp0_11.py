import threading
# Test threading daemonized threads
from pychirp.runtime import Runtime
from pychirp.properties import IntegerProperty

import pytest


class TestThreadMonitor(object):

    class IntThread(Runtime):
        test_prop = IntegerProperty()

    def test_setting_properties(self):
        with TestThreadMonitor.IntThread() as mon:

            with pytest.raises(RuntimeError):
                mon.test_prop = 10
            assert mon.test_prop is None

    def test_io_handler_change(self):

        ioclass = type("TestIO", (), {})()
        with TestThreadMonitor.IntThread(io_handler=ioclass) as mon:
            assert mon.io_handler_class is ioclass

        ioclass2 = type("TestIO2", (), {})()
        with pytest.raises(RuntimeError):
            with TestThreadMonitor.IntThread(io_handler=ioclass), \
                 TestThreadMonitor.IntThread(io_handler=ioclass2):
                mon.io_handler_class = ioclass2
