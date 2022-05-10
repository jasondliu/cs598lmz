import threading
threading.Thread(target=runserver, args=(web_port,)).start()

# Start the web interface
import os
os.system('chrome http://localhost:%d/' % web_port)
