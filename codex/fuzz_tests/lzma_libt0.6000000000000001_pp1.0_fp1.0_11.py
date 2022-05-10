import lzma
lzma.open
import bz2
bz2.open
import zipfile
zipfile.open
import tarfile
tarfile.open

import sqlite3
sqlite3.connect
import psycopg2
psycopg2.connect
import cx_Oracle
cx_Oracle.connect
import mysql.connector
mysql.connector.connect

import smtplib
smtplib.SMTP
import http.client
http.client.HTTPConnection
import ftplib
ftplib.FTP

# Test the above imports to make sure they're working
# This is useful for debugging if one of the imports failed
for var in dir():
    if var.startswith('_'):
        continue
    obj = eval(var)
    if hasattr(obj, '__name__'):
        print(obj.__name__)
    else:
        print(var)
