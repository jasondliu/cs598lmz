import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5 import QtWidgets
from mainwindow import MainWindow

from glob import glob as glb
from scipy.io import savemat, loadmat
from argparse import ArgumentParser


def create_directory(directory):
    """
    Function that creates a directory, if one does not yet exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def parse_args():
    parser = ArgumentParser(
        description="Run the main application of the MESS-C toolkit.")
    parser.add_argument('--loadplots', action='store_true',
                        help="load the graph plots from previous session")
    parser.add_argument('--debug', action='store_true',
                        help="run the application in debug mode")
    return parser.parse_args()


def create_template(template, target_file):
    """
    Create a file from template with appropriate place holders in the file name.
    """
   
