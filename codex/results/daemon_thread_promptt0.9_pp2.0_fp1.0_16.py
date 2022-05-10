import threading
# Test threading daemon
import random
import urllib2
import requests
#requests = requests.session()
import json
import os.path
import time
import ssl
import logging
import argparse

logging.basicConfig(level=logging.DEBUG,
                    format='(%(asctime)s) %(funcName)s %(levelname)s %(message)s')

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#sys.path.append(__location__)

log = logging.getLogger('server')

# Verify SSL certs
requests.packages.urllib3.disable_warnings()

LIST_QUERY = """{node(func:type(Article)) @filter(has(text) AND size(text) > 100) {
  langs:lang
  text
  id
}}"""


def main():
    """
    Main function.
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.
