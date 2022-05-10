import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from argparse import ArgumentParser
from . import __version__
from .cli import main
from .dataset import Dataset
from .dataset import DEFAULT_CONFIG_FILE

def get_args(argv=None):
    parser = ArgumentParser(prog='fcm', description=('The Flow Cytometry '
                             'Standard (FCS) file format is a standard file '
                             'format used by flow cytometers. The flowCore '
                             'package provides a fast, flexible framework for '
                             'manipulating flow cytometry data in R. The '
                             'flowClust package provides a set of tools for '
                             'clustering and visualization of flow data.'))
    parser.add_argument('-v', '--version', action='version',
                        version='fcm ' + __version__)
    parser.add_argument('-c', '--config', type=str,
                        default=DEFAULT_CONFIG_FILE, help=('configuration file
