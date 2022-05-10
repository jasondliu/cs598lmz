import types
types.MethodType(lambda self: self.set_value(self.get_value()), wx.SpinCtrl, wx.SpinCtrl.__init__)

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title)
        panel = wx.Panel(self, -1)
        self.sc = wx.SpinCtrl(panel, -1, "", size=(60,-1))
        self.sc.SetRange(0, 100)
