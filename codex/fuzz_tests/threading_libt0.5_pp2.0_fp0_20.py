import threading
threading.Thread(target=lambda: input()).start()

import os
import sys

sys.path.append(os.getcwd())

from server.main import app

app.run(host='0.0.0.0', port=5000, debug=True)
