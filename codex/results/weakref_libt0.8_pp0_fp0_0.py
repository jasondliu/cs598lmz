import weakref

class MyFileMessenger(ms.FileMessenger):
    def __init__(self, crt):
        self.crt = weakref.ref(crt)
        super().__init__()
    def __del__(self):
        super().__del__()
        self.crt().file_messenger = None
    def msg(self, msg):
        self.crt().msg_received(msg)

class Dialog(wx.Frame):
    """
    This class will be used to display the file messenger
    """
    def __init__(self, parent, title, size=None, pos=None, style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL):
        """
        parent: Parent window
        title: Window title
        size: Window size in pixels (width, height)
        pos: Window position in pixels (x, y)
        style: Window style
        """
        wx.Frame.__init__(self, parent, title=title, size=size, pos=pos, style=style
