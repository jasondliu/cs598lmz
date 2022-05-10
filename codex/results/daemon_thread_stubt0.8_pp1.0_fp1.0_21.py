import sys, threading

def run():
    sys.stdout.write("extension loaded")
sys.stdout = sys.stdout.flush()
thread = threading.Thread(target=run)
thread.start()

import requests

response = requests.get("http://localhost:3000")

sys.stdout.write(response.text)
</code>

