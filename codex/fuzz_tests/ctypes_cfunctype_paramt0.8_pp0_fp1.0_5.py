import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Test(unittest.TestCase):
    
    def test_platform(self):
        # Test platform-specific things
        p = sys.platform
        if p == 'darwin':
            self.assertEqual(GetApplicationPath(), '/')
            self.assertEqual(GetApplicationName(), 'Python')
        else:
            self.assertEqual(GetApplicationPath(), '/System/Library/Frameworks/Python.framework/Versions/Current')
            self.assertEqual(GetApplicationName(), 'Python')

        self.assertFalse(IsMainThread())

    def test_app(self):
        # Test application delegates
        # Get a reference to the shared application object
        app = NSApp()
    
        # Install an application delegate
        delegate = AppDelegate.alloc().init()
        app.setDelegate_(delegate)
    
        # This is needed to init the app
        AppHelper.runEventLoop()
        
        self.assertTrue(delegate.didFinishLaunchingCalled)
        self.assertEqual(delegate.name, 'Python
