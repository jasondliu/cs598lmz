import bz2
bz2.BZ2File('../data/sample.bz2')

import gzip
gzip.open('../data/sample.gz')

import zipfile
zipfile.ZipFile('../data/sample.zip')

import lzma
lzma.open('../data/sample.xz')

import sqlite3
connection = sqlite3.connect('../data/sample.sqlite')

import pyodbc
connection = pyodbc.connect('DSN=ODBC_DB;UID=user;PWD=pass')

import mysql.connector
connection = mysql.connector.connect(user='user',password='pass',host='127.0.0.1',database='sample')

import mysqldb
connection = mysqldb.connect(user='user',passwd='pass',host='127.0.0.1',db='sample')

import cx_Oracle
connection = cx_Oracle.connect('user/pass@127.0.0.1/sample')

import pymssql
connection = pymssql.connect(user='
