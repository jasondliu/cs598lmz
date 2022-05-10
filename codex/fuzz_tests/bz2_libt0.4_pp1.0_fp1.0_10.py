import bz2
bz2.BZ2Compressor()

import csv
csv.reader(open('file.csv'))

import datetime
datetime.date

import decimal
decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')

import difflib
difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])

import doctest
doctest.testmod()

import email
email.message_from_string('...')

import filecmp
filecmp.cmp('file1', 'file2')

import fnmatch
fnmatch.fnmatch('foo.txt', '*.txt')

import fractions
fractions.Fraction(1, 3)

import gzip
gzip.GzipFile('file.gz')

import hashlib
hashlib.md5('foo').digest()

import hmac
hmac.new('secret-shared-key-goes-here', 'The quick brown
