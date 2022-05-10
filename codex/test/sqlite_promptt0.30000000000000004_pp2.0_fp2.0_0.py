import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/test.db")
import time
import sys
import os
import subprocess
import RPi.GPIO as GPIO
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import datetime
import socket
import urllib2
import json
import requests

# GPIO pin numbers
GPIO_PIN_NUMBER_OF_CONTROL_1 = 18
GPIO_PIN_NUMBER_OF_CONTROL_2 = 23
GPIO_PIN_NUMBER_OF_CONTROL_3 = 24
GPIO_PIN_NUMBER_OF_CONTROL_4 = 25
GPIO_PIN_NUMBER_OF_CONTROL_5 = 12
GPIO_PIN_NUMBER_OF_CONTROL_6 = 16
GPIO_PIN_NUMBER_OF_CONTROL_7 = 20
GPIO_PIN_NUMBER_OF_CONTROL_8
