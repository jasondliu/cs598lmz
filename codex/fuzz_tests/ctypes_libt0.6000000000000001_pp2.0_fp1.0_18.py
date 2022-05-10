import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="png test")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.CenterOnScreen()

        # Set the background colour of the frame
        self.SetBackgroundColour(wx.Colour(255,255,255))

        # Load the image
        self.image = wx.Image('test.png')

        # Create a bitmap from the image
        self.bitmap = wx.Bitmap(self.image)

        self.SetClientSize(self.bitmap.GetSize())

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 0, 0)

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
