import weakref

import gizeh


class ScrolledPanel(wx.Panel):
    def __init__(self, parent, **kw):
        kw["style"] = kw.setdefault("style", wx.VSCROLL | wx.TAB_TRAVERSAL | wx.BORDER_DOUBLE) | wx.FULL_REPAINT_ON_RESIZE

        wx.Panel.__init__(self, parent, **kw)

        self.BackgroundColour = self.GetParent().GetBackgroundColour()

        self.SetAutoLayout(True)
        self.SetupScrolling()

        self.Bind(wx.EVT_SIZE, self.OnSize, self)

    def OnSize(self, event):
        self.Layout()
        self.SetupScrolling()


class TabPanel(ScrolledPanel):
    def __init__(self, parent, page, shared_data, **kw):
        ScrolledPanel.__init__(self, parent, **kw)

        self.page = page
        self.shared_data = shared_data
