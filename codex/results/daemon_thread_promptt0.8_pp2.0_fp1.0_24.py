import threading
# Test threading daemon
import daemon
import logging
logger = logging.getLogger(__name__)

# Local imports
import aardvark.libs.aard as aard


# Threading object
class AardvarkThread(threading.Thread):
    """
    A thread that runs the aardvark program.
    """

    def __init__(self, args={'master-channel': False}):
        threading.Thread.__init__(self)
        self.args = args
        self.error = False
        self.error_msg = None

    def run(self):
        try:
            logger.debug("AardvarkThread.run()")
            with daemon.DaemonContext():
                aard.main(self.args)
        except Exception as e:
            self.error = True
            self.error_msg = e


def main():
    # Create AardvarkThread object
    logger.debug("Creating thread")
    aard_thread = AardvarkThread()

    # Start threading
    logger.debug("Starting thread")
   
