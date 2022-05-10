import types
# Test types.FunctionType - for example, test_win32all
# tests win32api.LoadLibrary by loading a DLL from c:\windows\system
# which may not exist, or may be some non-PE image.  Therefore, we
# need to "work around" it...
class LoadLibraryTests(unittest.TestCase):
    def tearDown(self):
        try:
            import win32api
            win32api.FreeLibrary = self.oldFreeLibrary
            del win32api.LoadLibrary
            del win32api.GetModuleHandle
            win32api.GetProcAddress.__code__ = self.oldCode
        except:
            pass
    def testTryToLoadWindowsSystem(self):
        # Note that if you are using ActivePython, the getModuleHandle
        # test may fail as it is normal for windows *not* to have yet
        # loaded a DLL for the first time.  This is usually something
        # like shlwapi.
        import win32api
        self.oldFreeLibrary = win32api.FreeLibrary
        def HACK_FreeLibrary(hLib):

