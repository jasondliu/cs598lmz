import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    select.select(a,a,a,1.0)

class App(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None)
        test_select_mutated()
        self.Close()


app = wx.PySimpleApp()
frm = App().Show()
app.MainLoop()
