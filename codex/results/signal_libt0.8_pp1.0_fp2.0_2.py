import signal
signal.signal(signal.SIGINT, handler)

# set up logging
logger = logging.getLogger('serverlog')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler() # console handler
ch.setLevel(logging.INFO)
logger.addHandler(ch)
fh = logging.FileHandler('../log/{}.log'.format(dt.now().strftime('%Y-%m-%d_%H-%M-%S'))) # file handler
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

def main():
	if len(sys.argv) > 1 and sys.argv[1] == 'test':
		# run tests on server
		logger.info('Running tests...')
		import tests
		tests.run()
		logger.info('Tests complete.')
	
	while running:
		global id_list
		global last_broadcast
		id_list = []
		last_broadcast
