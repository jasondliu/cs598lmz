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
