import threading
# Test threading daemon
class HelpThread(threading.Thread):
	def __init__(self, target, *args):
		self._target = target
		self._args = args
		threading.Thread.__init__(self)
		
	def run(self):
		self._target(*self._args)

class App:
	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		self.button = Button(
			frame, text="QUIT", fg="red", command=frame.quit
			)
		self.button.pack(side=LEFT)

		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)

		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)

		self.hi_there = Button(frame, text="Hello", command
