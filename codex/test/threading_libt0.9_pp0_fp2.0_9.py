import threading
threading.stack_size(4096)

class MainApp:
		
	def __init__(self):
		self.MainWindow = Tk()
		self.MainWindow.title('Menubar')
		self.MainWindow.geometry('300x200')
		self.frame = Frame(self.MainWindow)
		self.frame.pack()
		
		self.m = Menu(self.MainWindow)
		self.MainWindow.config(menu=self.m)
		
		self.filemenu = Menu(self.m)
		self.m.add_cascade(label="File", menu=self.filemenu)
		self.filemenu.add_command(label="New project", command=self.newproject)
		self.filemenu.add_command(label="New...", command=self.new)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.MainWindow.quit)
		
