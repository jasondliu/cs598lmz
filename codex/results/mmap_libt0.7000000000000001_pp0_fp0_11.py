import mmap
import os
import time
import threading
import subprocess
from queue import Queue
from time import sleep
from tqdm import tqdm
from multiprocessing import Process, Manager
from colorama import Fore, Back, Style
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import json
import re

from modules.misc import print_line, print_color, print_warning, print_error, print_success
from modules.files import write_file, read_file, file_exists, make_directory
from modules.network import print_info
from modules.config import Config
from modules.tor import Tor
from modules.shodan import Shodan
from modules.censys import Censys
from modules.zoomeye import ZoomEye

"""

EXTERNAL MODULES

"""

def main():
    try:
        config = Config()
        print_color(" ")
        print_color("  PORT SCANNER")
        print_color("  ------------")
        print_color(" ")
        print_color("     Version
