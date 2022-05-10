import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import string
import unicodedata
import argparse
import subprocess

from . import utils

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

def main():
    """
    Main function
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Clean a text file")
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="Input file",
                        required=True)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="Output file",
                        required=True)
    parser.add_argument("-c", "--clean",
                        dest="clean",
                        help="Clean file",
                        required=False,
                        action="store_true")
    parser.add_argument("-s", "
