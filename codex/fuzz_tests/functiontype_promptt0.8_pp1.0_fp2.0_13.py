import types
# Test types.FunctionType for Python 2
import io
from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock

from parameterized import parameterized

from siptools.tests.utils import TestCase


logging.basicConfig(level=logging.DEBUG)


class MockW1(object):
    """Mocked W1ThermSensor class that simulates all temperature sensors
    returning 20.0 degrees.
    """
    @staticmethod
    def get_available_sensors():
        """Mock get_available_sensors method. Returns list of all available
        sensors.
        :returns: list -- List of W1ThermSensor objects
        """
        return [MockW1('1'), MockW1('2')]

    def __init__(self, sn):
        self.sn = sn

    def get_temperature(self, sensortype=None):
        """Mock get_temperature method. Returns sensor temperature.
        :returns: float -- Temperature in Decimal
        """
        return Decimal('20.0')


class MockDS
