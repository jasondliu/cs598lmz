import threading
# Test threading daemon
import time
import os
import sys
sys.path.append(os.getcwd())
from lib.config import get_config
from lib.logger import get_logger

# TODO remove this shit
from lib.utils import make_file_path

# TODO remove this shit
from lib.utils import make_file_path

def run_test():
    # Create a test logger
    logger = get_logger(__name__)
    # Create a test config
    config = get_config('test.yml')

    # Create a test thread
    my_thread = threading.Thread(target=test_thread, args=(logger, config))
    # Set it as a daemon thread
    my_thread.daemon = True
    # Start the test thread
    my_thread.start()

    # Test thread for 5 seconds
    time.sleep(5)
    # Stop the thread
    logger.info('Stopping the thread')
    my_thread.stop()
    # Wait for the thread to stop
    my_thread.join()
    # Say we are
