import bz2
bz2.BZ2File('test.bz2')

# csv
import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# tar
import tarfile
with tarfile.open('test.tar', 'r') as f:
    f.extractall()

# zip
import zipfile
with zipfile.open('test.zip', 'r') as f:
    f.extractall()

# base64
import base64
with open('test.jpg', 'rb') as f:
    data = f.read()
    print(base64.b64encode(data))

# hashlib
import hashlib
with open('test.txt', 'rb') as f:
    data = f.read()
    print(hashlib.md5(data).hexdigest())
    print(hashlib.sha1(data).hexdigest())
    print(hashlib.sha256(data).hexdigest())

# hmac

