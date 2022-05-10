import mmap
import requests
import argparse
import datetime
import xml.etree.ElementTree as et
import time
import sys
import re

# Local imports
import config

# Globals
default_login_url = "https://accounts.google.com/ServiceLogin"
default_auth_url = "https://accounts.google.com/ServiceLoginAuth"
default_service_url = "htts://mail.google.com/mail/feed/atom"
default_mail_url = "https://mail.google.com/mail/#inbox"
default_date_format = "%a, %d %b %Y %H:%M:%S"
gmail_id = 1


class GmailException(Exception):
    """ Base exception class for this module
    """
    pass

