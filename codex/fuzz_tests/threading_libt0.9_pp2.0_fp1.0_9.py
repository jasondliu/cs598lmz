import threading
threading.Thread(group=None, target=telnet_thread, name=None).start()
threading.Thread(group=None, target=flourish_thread, name=None).start()

@app.route("/healthz")
def healthz():
	return ""

@app.route("/")
def hello():
	return "Hello!"

@app.route("/intro")
def intro():
	return render_template('intro.html')

@app.route("/stage")
def stage_it():
	return render_template('stage.html')

@app.route("/flourish")
def flourish():
	global flourish_mode
	flourish_mode = True
	return "<h1 style='color:red;'>Flourish!</h1>"

@app.route("/on")
def on():
	global telnet
	telnet.write("\r\n")
	return "<h1 style='color:green;'>ON!</h1>"

@app.route("/off")
def off():
	
