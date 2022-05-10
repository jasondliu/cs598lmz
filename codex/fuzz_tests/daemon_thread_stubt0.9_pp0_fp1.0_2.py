import sys, threading

def run():
	admin.socketio.run(admin.app, host='127.0.0.1', port=6000, debug=True)

def outer_run():
	def run():
		admin.socketio.run(admin.app, host='127.0.0.1', port=6000, debug=True)
	
	try:
		t = threading.Thread(target=run)
		t.setDaemon(True)
		t.start()
	except:
		print "Uh oh, couldn't start socketio thread :("

def to_str(something):
	try:
		return something.__str__
	except:
		return something
