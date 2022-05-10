import types
types.MethodType(lambda self: self.set_value(self.get_value()),
                 wx.SpinCtrl, wx.SpinCtrl)

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a SpinCtrl", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        win = wx.SpinCtrl(self, -1, "", (50, 50), (80, -1))
        win.SetRange(0, 100)
        win.SetValue(5)
        win.SetFocus()


#---------------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#---------------------------------------------------------------------------


overview = """\
<html><body>
