import socket
from time import sleep
import os

def read_file(file):
    with open(file, 'r') as f:
        return ''.join(f.readlines())

pwd = read_file(os.path.dirname(os.path.abspath(__file__)) + '/pwd.conf').strip()

def read_account(file):
    account = read_file(file)
    return account.split(',')

def check_account_file(file):
    if not os.path.isfile(file):
        with open(file, 'w+') as f:
            f.write('')

def validate_ssl(cert, host):
    cert = ssl.get_server_certificate((host, 443))
    x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    return x509.get_subject().CN

# log in to wireless router
post_data = {
     'username' : '',
     'password' : '',
     'ajax' : 1

