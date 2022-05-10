import lzma
lzma.open
from lzma import LZMAFile
import os
from os import listdir
from os.path import isfile, join
import sys
from sys import argv
import time
from time import sleep
import traceback
from tqdm import tqdm
import urllib.request
from urllib.request import urlretrieve
from urllib.request import urlopen

from config import *

# Script starts here

# Check for, and create if needed, the directory for the downloaded files
if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# Check for, and create if needed, the directory for the extracted files
if not os.path.exists(EXTRACT_DIRECTORY):
    os.makedirs(EXTRACT_DIRECTORY)

# Get the current directory
current_directory = os.getcwd()

# Change the current directory to the download directory
os.chdir(DOWNLOAD_DIRECTORY)

# Get the list of files in the download
