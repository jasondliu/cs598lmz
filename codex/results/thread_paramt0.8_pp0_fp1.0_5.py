import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

##############
# In bash, run: pip3 install websocket-client
# And then run: python3 ws.py
# In a separate terminal
# run: python3 ws-server.py
#
# To run the client.
#
# Add the client class to your project and
# call the on_message callback as messages
# are received.

from websocket import create_connection
import json

class Client:
    def on_message(self, message):
        # Override with the message handler
        print(message)

    def ws_runner(self):
        ws = create_connection("ws://localhost:8080/ws")

        while True:
            try:
                message = json.loads(ws.recv())
                self.on_message(message)
            except Exception as e:
                print(str(e))
                break

    def start(self):
        t = threading.Thread(target=self.ws_runner)
        t.start()
