import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
	# This is a way to get the path to the source directory.
	# See http://stackoverflow.com/a/6098238
	root_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
	os.chdir(root_dir)

	# Update configuration file
	try:
		config.update(os.path.join(root_dir, 'config.json'))
	except Exception, e:
		print 'Unable to load config.json: %s' % e
		sys.exit(1)

	# Start the application
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()
