import mmap
import sys
import os
import re
import csv
import time
import datetime
import subprocess
import argparse
import logging
import logging.handlers
import json
import signal

#
# Main
#

def main():
    #
    # Parse command line arguments
    #

    parser = argparse.ArgumentParser(description='Run a hdfs command and log the results to a csv file.')

    parser.add_argument('--hdfs-cmd', help='hdfs command to run', required=True)
    parser.add_argument('--hdfs-cmd-args', help='hdfs command arguments', required=True)
    parser.add_argument('--csv-file', help='csv file to write results to', required=True)
    parser.add_argument('--log-file', help='log file to write results to', required=True)
    parser.add_argument('--log-level', help='log level', default='INFO')
    parser.add_argument('--log-max-bytes', help='log max bytes', default='1
