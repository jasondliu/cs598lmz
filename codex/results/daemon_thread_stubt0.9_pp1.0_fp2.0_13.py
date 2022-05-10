import sys, threading

def run():
			# now start up the server
			server = SimpleXMLRPCServer(("localhost", 9000),
										requestHandler=RequestHandler)
			server.register_introspection_functions()
			try:
					thread = threading.Thread(target=server.serve_forever)
					thread.start()
					time.sleep(1)
					print "Server running"
					runTests()
			finally:
					server.stopThread = True

def runTests():
			server = ServerProxy("http://localhost:9000")

			import datetime
			args = [1,2.2,'three',4,5.5,
					{"a":"b"},
					["a", "b", 12, 12.2, {"a":"b"}, ("c", "d")],
					("a", "b", 12
