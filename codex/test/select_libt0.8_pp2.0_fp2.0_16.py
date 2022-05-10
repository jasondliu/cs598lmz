import select, sys, multiprocessing, subprocess, Queue, datetime, time
import os
import re

import json
import requests

import argparse

try:
    from urllib.parse import urlparse
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urlparse
    from urlparse import urljoin

parser = argparse.ArgumentParser(description='OAI Harvester :: Harvest repository and send records via SCAPE Harvester')

parser.add_argument('harvest_dir', action="store",
                    help='Temp directory to store the harvested metadata')
parser.add_argument('harvester_url', action="store",
                    help='URL to the Harvester service')
parser.add_argument('repo', action="store",
                    help='Repository ID in the Harvester service')
parser.add_argument('base_url', action="store",
                    help='Base URL to the OAI repository')
parser.add_argument('metadata_prefix', action="store",
                    help='Metadata prefix to harvest')
