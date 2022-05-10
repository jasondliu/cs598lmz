import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.SetBackgroundColour('white')

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.canvas = wx.glcanvas.GLCanvas(self, style=wx.FULL_REPAINT_ON_RESIZE)

        sizer.Add(self.canvas, 1, flag=wx.EXPAND)

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

        self.camera_look = [0.0, 0.0, 0.0]
        self.camera_
