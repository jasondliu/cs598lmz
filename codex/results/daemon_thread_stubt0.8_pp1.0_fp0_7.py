import sys, threading

def run():
	root = Tk()
	app = App(root)
	root.mainloop()

def start():
	t = threading.Thread(target=run)
	t.daemon = True
	t.start()

class App(object):
	def __init__(self, root):
		self.root = root
		self.root.geometry("200x200")

		self.var = IntVar()
		self.var.set(1)
		self.label = Label(self.root, textvariable=self.var)
		self.label.pack(side="top")

		self.button1 = Button(self.root, text="start", command=self.start, width=35)
		self.button1.pack(side="top")
		self.button2 = Button(self.root, text="stop", command=self.stop, width=35)
		self.button2.pack(side="top")

	def start(self):
		self.root.after(1000, self.callback)

	
