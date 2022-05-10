import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/converting-a-python-script-into-a-service
# https://www.ibm.com/developerworks/aix/library/au-threadingpython/

class IridiumTracker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.name = "iridium_tracker"

    def run(self):
        while True:
            time.sleep(1)
            logging.debug("iridium_tracker running")


# https://stackoverflow.com/questions/19071512/converting-a-python-script-into-a-service

class IridiumServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.name = "iridium_server"

    def run(self):
        print("Starting Iridium server thread")
        server = iridium
