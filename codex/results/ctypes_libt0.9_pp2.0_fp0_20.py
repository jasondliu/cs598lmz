import ctypes
ctypes.windll.user32.SetProcessDPIAware()
from PIL import ImageGrab
import win32api, win32con

class KeyMonitor():
    def __init__(self):
        self.keys = ['p', 'q']
        self.state = set()
        for key in self.keys:
            self.state.add(key)

    def GetKeys(self):
        return self.state

    def KeyDown(self, key):
        self.state.add(key)

    def KeyUp(self, key):
        if key in self.state:
            self.state.remove(key)

    def AddKey(self, key):
        self.keys.append(key)

km = KeyMonitor()

def OnKeyboardEvent(event):
    if event.KeyID == win32con.WM_KEYDOWN:
        km.KeyDown(chr(event.Ascii).lower())
    elif event.KeyID == win32con.WM_KEYUP:
        km.KeyUp(chr(event.Ascii).lower())
   
