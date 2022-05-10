import threading
threading.Thread(target=lambda: None).start()

# Start the web server
from bottle import run
