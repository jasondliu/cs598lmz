import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import time
import os
import sys
import logging
import logging.handlers
import argparse
import re
import platform
import psutil
import subprocess

# TODO:
# - Add a "debug" mode that doesn't do any of the real work, but just prints out what it would do.
# - Add a "verbose" mode that prints out all the details of what it's doing.
# - Add a "dry-run" mode that doesn't actually do anything, but prints out what it would do.
# - Add a "quiet" mode that doesn't print anything out.
# - Add a "progress" mode that prints out a progress indicator as it's running.
# - Add a "version" command that prints out the version number and exits.
# - Add a "help" command that prints out the help and exits.
# - Add a "list" command that lists all the available commands.
# - Add a "show" command that shows the details of a specific command.
# - Add a "list-options" command that lists all the available options.
# - Add
