import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys

#----------------------------------------------------------------
# the a.sys branch
if __name__ == "__main__":
    # first, we check to be sure we are running the right version of Python
    if sys.version_info < (3,4):
        sys.exit("This program requires Python 3.4 and above.  Go to http://python.org/")
    # next, we add to the PYTHONPATH the ITK-PingPong library root directory
    #sys.path.append(os.path.join(os.path.expanduser("~"), "ITK-Remote-Module-Builds", "ITKPingPong", "lib"))
    # next, we add to the PYTHONPATH the ITK-PingPong library root directory
    if 'ITK_AUTOLOAD_PATH' in os.environ:
        pass
    elif os.name == 'nt':
        os.environ['ITK_AUTOLOAD_PATH'] = os.path.join
