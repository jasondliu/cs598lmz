import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class main(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(main, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		self.SetSize((600, 400))
		self.SetTitle("Sqlite3 Database Editor")
		self.Centre()
		self.Show(True)


def main():
	ex = wx.App()
	main(None)
	ex.MainLoop()

if __name__ == "__main__":
	main()
