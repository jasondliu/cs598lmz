import select
+import signal
+import time
+import sys
+
+try:
+    import requests
+    import socketio
+    import eventlet
+    from flask import Flask
+    from flask_socketio import emit
+    from pathlib import Path
+
+except Exception as e:
+    print("ERROR: missing library: {}\nInstall with 'pip install requests eventlet flask flask_socketio path'".format(e))
+    sys.exit(1)
+
+
+PROJECT_LIBSYTEMS_RUN_PATH = Path("/var/lib/sytems/run")
+
+app = Flask(__name__)
+app.config['SECRET_KEY'] = 'secret!'
+io_app = socketio.Middleware(socketio.Server(logger=False, async_mode='eventlet'), app)
+
+
+def load_agent(agent_name):
+    output = None
+    try:
+        output = subprocess.check_output("systemctl show %s" % agent_name,
+                
