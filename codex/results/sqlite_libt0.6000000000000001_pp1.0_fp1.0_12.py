import ctypes
import ctypes.util
import threading
import sqlite3
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os import listdir
from os.path import isfile, join

# Variables
# 
# # Filepaths
# filepath_config = "C:\\Users\zach\Desktop\Projects\Python\Dictionary\config.ini"
# filepath_database = "C:\\Users\zach\Desktop\Projects\Python\Dictionary\database.db"
# filepath_log = "C:\\Users\zach\Desktop\Projects\Python\Dictionary\log.txt"
# filepath_debug = "C:\\Users\zach\Desktop\Projects\Python\Dictionary\debug.txt"
# 
# # Dictionary
# dictionary = {}
# 
# # Other
# current_word = ""
# current_definition = ""
# current_id = ""
# current_timestamp
