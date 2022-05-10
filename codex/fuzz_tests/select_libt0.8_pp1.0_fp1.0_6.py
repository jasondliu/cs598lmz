import select
import socket
import sys
import time
import datetime
import random
import os
import pickle
import logging
import logging.handlers
import subprocess
import zlib
import json
import base64
import pandas as pd
import numpy as np
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#------------------------------------------------------------------------------------------------------------
#
# Script start
#
logging.basicConfig(filename='/var/opt/nagios/nagiosgrapher.log',  format='%(asctime)s %(message)s', level=logging.INFO)

#------------------------------------------------------------------------------------------------------------
#
# Getting data from Nagios
#
def get_perfdata(host, service):

    perfdata = {}
    perfdata['hostname'] = host['host_name']
    perfdata['servicename'] = service['service_description']
