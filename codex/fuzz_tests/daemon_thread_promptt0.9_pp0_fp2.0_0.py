import threading
# Test threading daemon functionality
# Test that threading does not increase memory usage
# Test that subprocess does not increase memory usage unless popen.communicate
# is called
import subprocess
import sys
from .__init__ import *

# Test whether we can correctly classify input correctly
# Test whether we can correctly classify output correctly


def start_test():
    """
        Ensure we have a directory to test in.
        Setup the db parameters.
        Start a process to act as a server.  Write commands to it and expect results.
    """
    ###
    ## Argument parsing
    ###
    import argparse
    parser = argparse.ArgumentParser(description='The papercut-notify daemon tester')
    parser.add_argument('-t', '--fail-threshold', default=2, type=int, help='The number of failures that can occur before aborting tests')
    parser.add_argument('-c', '--check-buffer', action='store_true', help='Turn on to check whether the output buffer matches input')
    parser.add_argument('-v', '--verbose', action='store_true
