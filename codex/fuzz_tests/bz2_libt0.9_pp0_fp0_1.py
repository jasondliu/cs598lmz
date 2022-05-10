import bz2
bz2.decompress(open(context.getCacheDir(), "/mnt/sdcard/cache.bz2").read())

import zipfile
zip = zipfile.ZipFile(context.getCacheDir(), '/mnt/sdcard/cache.zip', 'r')
zip.extractall(context.getCacheDir(), '/mnt/sdcard/cache/')
zip.close()

import tarfile
tar = tarfile.open(context.getCacheDir(), '/mnt/sdcard/cache.tar', 'r')
tar.extractall(context.getCacheDir(), '/mnt/sdcard/cache')
tar.close()

import base64
base64.b64decode(open(context.getCacheDir(), "/mnt/sdcard/cache.b64").read())

import sqlite3
conn = sqlite3.connect(context.getCacheDir() + '/mnt/sdcard/cache.db')
c = conn.cursor()
c.execute('SELECT * FROM injection')
print c.fetchall()
conn.commit()
conn.close()
