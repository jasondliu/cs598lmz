import gc, weakref

from twisted.trial import unittest
from twisted.internet import reactor, defer

from foolscap.api import eventually
from foolscap.tokens import BulkDataToken, BananaError
from foolscap.referenceable import Referenceable

class Banana(unittest.TestCase):
    def testBananaError(self):
        # make sure this doesn't raise an exception
        be = BananaError("hi")
        be.trap(BananaError)


class BananaInterfaces(unittest.TestCase):
    def test_IBanana(self):
        from foolscap.banana import IBanana
        from foolscap.banana import Banana
        assert IBanana.implementedBy(Banana)

    def test_IBananaIndentation(self):
        from foolscap.banana import IBanana
        from foolscap.banana import BananaIndentation
        assert IBanana.implementedBy(BananaIndentation)

    def test_IBananaFailure(self):
        from foolscap.banana import IBan
