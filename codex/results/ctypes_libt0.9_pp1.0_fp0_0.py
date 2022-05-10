import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/hcl/libhcl.so')

from twhcl import *
import twhcl;

class MyWindow(twhcl.Window):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.paint_event += self.on_paint
        self.resize_event += self.on_resize
        self.mouse_drag_event += self.on_mouse_drag
        self.wnd_show_event += self.on_show

    def on_show(self, wnd):
        self.set_icon('icon.png')
        pass

    
