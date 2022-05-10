import signal
signal.signal(signal.SIGTERM, handler)

# Retrieve the options
options = get_options()

# Start the server
server = Server(options)
server.start()
