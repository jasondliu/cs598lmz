import socket
import time
import sys
import os
import re
import threading
import paramiko
import logging
import datetime
import traceback
import getpass
import random
import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/home/dba/log/sftp_download.log',
                    filemode='a')

def get_remote_file(hostname, username, password, port, remotepath, localpath):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remotepath, localpath)
    t.close()

def put_remote_file(host
