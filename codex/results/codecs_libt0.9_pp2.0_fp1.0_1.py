import codecs
codecs.register(codecs.lookup("imap4_utf_7"))
import imaplib
from imaplib_connect import open_connection
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from os import walk
from os.path import join, splitext
from io import BytesIO
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.encoders import encode_base64
from apiclient import errors


# Login and connection function with Gmail
def main():
    # Selecting this boxes
    box_list = ['INBOX']
    # User credentials to access Gmail API
    SCOPES = 'https://mail.google.com/'
    # Connect to Gmail API
    store = file.Storage('/home/alex/PycharmProjects/test/token.json')
    creds = store.get()
    if not cred
