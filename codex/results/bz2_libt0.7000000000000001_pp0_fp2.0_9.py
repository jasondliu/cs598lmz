import bz2
bz2.__version__

import csv
csv.__version__

import datetime
datetime.datetime.now()
datetime.__version__

import email
email.__version__

import filecmp
filecmp.dircmp('test', 'test1')
filecmp.__version__

import fnmatch
fnmatch.fnmatch('foo.txt', '*.txt')
fnmatch.__version__

import glob
glob.glob('*.py')
glob.__version__

import gzip
gzip.__version__

import hashlib
hashlib.md5(b'Hello Python').hexdigest()
hashlib.__version__

import hmac
hmac.new(b'Hello', b'Python').hexdigest()
hmac.__version__

import imaplib
imaplib.IMAP4('imap.gmail.com').list()
imaplib.__version__

import inspect
inspect.getmembers(inspect)
inspect.__version__

import json
json.dumps({'
