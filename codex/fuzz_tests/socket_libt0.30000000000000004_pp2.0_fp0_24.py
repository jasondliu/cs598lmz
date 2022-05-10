import socket
import sys
import os
import time
import threading
import re
import json
import random
import string
import base64

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util import Counter

# TODO:
# - Add a way to send a message to all users
# - Add a way to send a message to a specific user
# - Add a way to send a message to a group of users
# - Add a way to send a message to a group of users excluding some users
# - Add a way to send a message to a group of users excluding some users, but including some other users
# - Add a way to send a message to a group of users excluding some users, but including some other users, and excluding some other users
# - Add a way to send a message to a group of users excluding some users, but including some other users, and excluding some other users, but including some other users
# - Add a way to send a message to a group of users excluding some users, but including some other users, and excluding some other users, but including some other users, and excluding some other users
# -
