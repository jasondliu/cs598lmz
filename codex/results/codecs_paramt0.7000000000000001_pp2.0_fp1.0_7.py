import codecs
codecs.register_error('strict', codecs.strict_errors)

from ml2h5.converters import *
from ml2h5.converters.base import *
from ml2h5.converters.matlab import MatlabData
from ml2h5.converters.h5matlab import H5MatlabData
from ml2h5.converters.h5python import H5PythonData
from ml2h5.converters.python import PythonData
from ml2h5.converters.exceptions import *


class TestConverter(TestCase):
    """
    Tests for the converter class
    """

    def setUp(self):
        self.converter = Converter()

    def test_default_keys(self):
        self.assertTrue(self.converter.input_key in self.converter.keys)
        self.assertTrue(self.converter.output_key in self.converter.keys)

    def test_set_keys(self):
        self.converter.input_key = 'test_
