import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
	# This is a way to get the path to the source directory.
	# See http://stackoverflow.com/a/6098238
	root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
	os.chdir(root_dir)

	# Update configuration file
