import threading
threading.Thread(target=lambda: None).start()

# Start the web server
from bottle import run
run(host='0.0.0.0', port=8080)
