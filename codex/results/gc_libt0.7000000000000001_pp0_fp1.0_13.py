import gc, weakref, os
import objc
from PyObjCTools.TestSupport import *
from PyObjCTest.testbndl import PyObjC_TestClass4
from PyObjCTest.testbndl import *

class OC_TestClass6(NSObject, OC_TestClass1, OC_TestClass3, OC_TestClass5,
        PyObjC_TestClass4):
    pass

class TestBundle2(TestCase):
    def testBundle2(self):
        if not hasattr(objc, 'loadBundle'):
            return

        bundle = objc.loadBundle('PyObjCTest', globals(),
                bundle_path=os.path.join(os.path.dirname(__file__),
                    'PyObjCTest.bundle'))
        self.assert_(bundle is not None)

        self.assert_(hasattr(bundle, 'OC_TestClass1'))
        self.assert_(hasattr(bundle, 'OC_TestClass3'))
        self.assert_(hasattr(bundle, 'OC_TestClass
