import socket
import time
import os
import sys
import threading
import random
import string
import platform
import subprocess
import re

# Define the colors we will use in the program
class colors:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    end = '\033[0m'

# Define the banner that will be displayed
def banner():
    print(colors.blue + '''
  ____        _   _   _           _     _      
 |  _ \      | | | | | |         | |   (_)     
 | |_) |_   _| |_| |_| | ___  ___| |__  _ _ __ 
 |  _ <| | | | __| __| |/ _ \/ __| '_ \| | '_ \
 | |_) | |_| | |_| |_| |  __/\__ \ | | | |
