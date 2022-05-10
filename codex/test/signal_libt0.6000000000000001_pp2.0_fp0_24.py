import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def start():
    global frame, frame_size
    frame = Frame(None)
    frame.SetTitle("Bubble Breaker")
    frame.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))
    frame.SetSize(frame_size)
    frame.Centre()
    frame.Show(True)
    app.MainLoop()

class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, size=(frame_size))
        #panel
        global panel
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("#FFFFFF")
        panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        panel.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        panel.Bind(wx.EVT_MOTION, self.OnMouseMove)

