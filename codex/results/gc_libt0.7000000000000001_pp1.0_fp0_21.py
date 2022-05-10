import gc, weakref, sys
from pympler.asizeof import asizeof
from pympler.util import get_referents
from pympler.tracker import SummaryTracker
from pympler import refbrowser

def _get_module_referents(module_name):
    referents = set()
    module = sys.modules[module_name]
    referents.update(get_referents(module.__dict__.values()))
    return referents

def _get_module_size(module_name):
    referents = _get_module_referents(module_name)
    size = asizeof(module_name)
    for referent in referents:
        size += asizeof(referent)
    return size

class TestRefbrowser(unittest.TestCase):

    def test_browser(self):
        """
        Test the refbrowser
        """
        tracker = SummaryTracker()

        import pympler.tests
        module_name = pympler.tests.__name__
        self.assertTrue(module
