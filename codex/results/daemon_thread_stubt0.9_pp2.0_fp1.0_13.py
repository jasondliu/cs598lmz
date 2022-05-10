import sys, threading

def run():
	yaml.add_multi_constructor('', multiobj)
	#ast = yaml.load(open(sys.argv[1]).read())
	ast = yaml.load(open('testbench.yml').read())
	# XXX should validate ast at this point. It's >50% of the
	# work to make the construction (and evaluation) of the job data
	# right.
	pt = ProcessorThread(job=ProcessingJob(ast))
	pt.start()
	try:
		while True:
			pt.join(1)
			print sys.stderr, 'Heartbeat'
	except KeyboardInterrupt:
		sys.exit(0)
		# may want to kill the child process?


class ProcessingJob:
	def __init__(self, ast):
		self._ast = ast

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			repr(self._ast),
			)
