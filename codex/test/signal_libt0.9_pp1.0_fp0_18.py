import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

s = Server(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        ".testing.db"), listen_port=8080, listen_ip="127.0.0.1")

# Insert a row and test
c = s.connection
