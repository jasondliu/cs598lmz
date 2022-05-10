import _struct

from . import io
from . import pep8
from . import pyflakes
from . import pyflakes_ext
from . import pyflakes_ext_test
from . import pyflakes_test
from . import pyflakes_test_test
from . import pyflakes_test_test_test
from . import ssl
from . import ssl_test
from . import ssl_test_test
from . import ssl_test_test_test
from . import test
from . import test_test
from . import test_test_test

# TODO: add tests for the following:
#  - imp.find_module()
#  - imp.load_module()
#  - imp.load_source()
#  - imp.load_compiled()
#  - imp.get_suffixes()
#  - imp.get_magic()
#  - imp.acquire_lock()
#  - imp.release_lock()


class TestCase(unittest.TestCase):

    def test_all(self):
        self.assertEqual
