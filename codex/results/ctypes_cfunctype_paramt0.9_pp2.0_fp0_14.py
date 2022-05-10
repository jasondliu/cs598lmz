import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import pyglet.window.xlib.xlib
xlib = pyglet.window.xlib.xlib
fun = FUNTYPE(pyglet.window.xlib.xlib._lib.XDestroyWindow)
xlib.XDestroyWindow.argtypes = [ctypes.c_void_p]
xlib.XDestroyWindow.restype = fun(xlib.XDestroyWindow)

opacity, background_color= 1, (0,0,0,255)
window_class_name, window_name, icon_name='MyClass', 'MyWindow', 'MyIcon'


if __name__ == '__main__':
    app = wx.App()
    screen= wx.ScreenDC()
    get_window_geometry = wx.Display.GetGeometry(wx.Display(0))
    width,height = (200,200) #(get_window_geometry[2], get_window_geometry[2])
    gl_attribs = (glcanvas.WX_GL_RGBA, # RGBA
                  gl
