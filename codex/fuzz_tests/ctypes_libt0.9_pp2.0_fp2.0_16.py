import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class customtoolbar(wx.Frame):

	def __init__(self, parent, title):
		super(customtoolbar, self).__init__(parent, title=title,
			size=(350, 250))

		self.InitUI()
		self.Centre()
		self.Show()     

	def InitUI(self):

		self.count = 0        

		tb = self.CreateToolBar()

		for i in range(15):
			tb.AddCheckLabelTool(i, '', wx.Bitmap('/home/zidan/Desktop/user_green.png'))

		tb.Bind(wx.EVT_TOOL, self.OnToolClick)
		tb.Realize()

		self.panel = wx.Panel(self)


	def OnToolClick(self, e):

		tool = e.GetEventObject().FindById(e.GetId())
		tool.SetBitmap(wx.Bit
