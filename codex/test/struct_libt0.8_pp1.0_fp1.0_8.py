import _struct
import array
import os
import sys
import argparse
import json
import sqlite3
import re

# Set up a command line parser:
parser = argparse.ArgumentParser(description='Dump a git repository as JSON data, so we can look at it in the web browser!')
parser.add_argument('repo', metavar='repo', type=str, help='Path to a Git repository')
parser.add_argument('--verbose', action="store_true", dest="verbose", help='Verbose mode')
parser.add_argument('--all', action="store_true", dest="all", help='Examine all refs')
parser.add_argument('--ref', action="store", dest="ref", help='Examine only the supplied ref')
parser.add_argument('--output', action="store", dest="output", help='Output file')
parser.add_argument('--db', action="store", dest="db", help='Output db')

# Init our variables:
args = parser.parse_args()
repository = args.repo

# Try
