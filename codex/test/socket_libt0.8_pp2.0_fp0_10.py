import socket
import time
import sys
import re
import os
import glob
import threading
import urllib
import hashlib
import imghdr
import Queue

# for assembling the transcript
import docx
from docx.shared import Pt
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK

# for sending the email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.Utils import COMMASPACE, formatdate

# for pynotify
import pynotify

# the data dir
data_dir = None

# the filetypes we want
