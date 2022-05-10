gi = (i for i in ())
# Test gi.gi_code = None.
gi.gi_code = None
# Test code creation.
class mycode(object):
	def __init__(self):
		self.co_argcount = 0
		self.co_code = "A"
		self.co_consts = ()
		self.co_filename = ""
		self.co_firstlineno = 0
		self.co_flags = 0
		self.co_freevars = ()
		self.co_name = ""
		self.co_names = ()
		self.co_nlocals = 0
		self.co_stacksize = 0
		self.co_varnames = ()

# Test generator creation.
class mygen(object):
	def __init__(self):
		self.gi_frame = None
		self.gi_running = False
		self.gi_code = None

# Test interpreter creation.
class myinterpreter(object):
	def __init__(self):
		self.callinfo = None

