import sys, threading

def run():
    while True:
        time.sleep(600)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

# Configure stuff
port = int(os.environ.get("PORT", 3000))
ip = os.environ.get("IP", "0.0.0.0")

# Start Flask app
app.run(host=ip, port=port, debug=True)
