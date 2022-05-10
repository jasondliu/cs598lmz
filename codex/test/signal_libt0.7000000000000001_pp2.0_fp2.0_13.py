import signal
signal.signal(signal.SIGINT, signal_handler)

# TODO: put into the config file
# TODO: make sure that these are effectively used
ACTION_THRESHOLD = 0.5
EYE_THRESHOLD = 0.5

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit("Usage: %s <action config file>" % sys.argv[0])

	config_path = sys.argv[1]
	with open(config_path) as f:
		config = yaml.load(f)

	# Init the different parts of the system.
	# Eye
