import sys, threading
threading.Thread(target=lambda:
                 sys.stdout.write('Fish\n')).start()


USE_WX = False

if USE_WX:
    # Mixin for making the window completly (or almost completly)
    # transparent

    import wx
    class TransparentWindowMixin:
        def __init__(self, alpha=wx.ALPHA_TRANSPARENT):
            self.alpha = alpha
            self.__in_paint = False

        def SetTransparent(self, alpha):
            self.alpha = alpha
            self.Refresh()

        def OnEraseBackground(self, event):
            """ Handles the wx.EVT_ERASE_BACKGROUND event. """

            if self.__in_paint or not self.HasTransparentBackground():
                event.Skip()
            
        def HasTransparentBackground(self):
            return self.alpha < 255

        def OnPaint(self, event):
            self.__in_paint = True

            if self.HasTransparentBackground():
                dc = wx.AutoBufferedP
