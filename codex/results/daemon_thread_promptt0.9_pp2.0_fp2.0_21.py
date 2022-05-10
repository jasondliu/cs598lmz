import threading
# Test threading daemon to communicate periodically with the server in the background
# If you are testing this script, make sure to comment the import and 'daemon.start()' line from the main script file
class Daemon(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            with urllib.request.urlopen(url) as response:
               html = response.read()
               out_str = str(html)
            print(out_str)
            time.sleep(5)

daemon = Daemon(5)
'''

def main():  
        # For communicating with the server
        with urllib.request.urlopen(url) as response:
            html = response.read()
            out_str = str(html)

if __name__ ==
