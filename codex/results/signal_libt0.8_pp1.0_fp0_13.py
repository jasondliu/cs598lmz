import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class App:
	def __init__(self):
		self.status = "startup"
		self.text = ""
		self.choice_list = []

	def main(self):
		if self.status == "startup":
			self.startup()
		elif self.status == "readfile":
			self.readfile()
		elif self.status == "get_input":
			self.get_input()
		else:
			self.invalid()

	def startup(self):
		print("Welcome to Text Adventure.\n")
		time.sleep(1)
		print("Would you like to load a saved state? [Y/n]")
		self.status = "get_input"

	def readfile(self):
		try:
			state = open("state.txt", "r")
			state_list = state.readlines()
		
