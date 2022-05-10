import types
types.IntType = int
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import subprocess
import socket
import signal
import time
import smtplib
import datetime
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders
import os
from time import strftime
import sys
from pprint import pprint
import sqlite3 as lite
from picamera import PiCamera

from threading import Thread

# global variables
curr_temp = 0
curr_hum = 0
curr_press = 0

# read in configuration file
with open('config.json') as data_file:
    config = json.load(data_file)

# setup email message
msg = MIMEMultipart()
msg['Subject'] = config["email_subject"]
msg['From'] = config["email_from"]
