import socket
import sys
import getopt
import threading
import subprocess
import hashlib
import os
import base64
import time

# global vars for the server
listen = False
command = False
upload = False
execute = False
target = ""
upload_destination = ""
port = 0

#define the usage
