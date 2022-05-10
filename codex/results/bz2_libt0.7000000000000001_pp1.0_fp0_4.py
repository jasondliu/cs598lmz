import bz2
bz2.BZ2Compressor

import gzip
gzip.GzipFile

import lzma
lzma.LZMACompressor

import zipfile
zipfile.ZipFile

import tarfile
tarfile.TarFile

# 4.2.2 文件的文本编码
import chardet
chardet.detect

import csv
csv.DictReader

import html
html.escape

import json
json.load

import xml.sax
xml.sax.parse

# 4.2.3 二进制数据
import base64
base64.b64encode

import binascii
binascii.crc32

import struct
struct.pack

import hashlib
hashlib.md5

# 4.3 网络
import ftplib
ftplib.FTP

import imaplib
imaplib.IMAP4

import smtplib
smtplib.SMTP


