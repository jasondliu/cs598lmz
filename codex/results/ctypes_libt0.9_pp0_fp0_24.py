import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

class SambaUpdateApp(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.iconbitmap('favicon.ico')
		self.badge = None
		self.title("Samba for Arduino - Update")
		self.geometry("410x420")
		self.minsize(410, 420)
		self.resizable(True, True)
		self.wm_state('zoomed')
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.update_idletasks()

		filemenu = Menu(self)
		filemenu.add_command(label="About", command=self.about_window)
		filemenu.add_command(label="Exit", command=self.on_exit)
		self.config(menu
