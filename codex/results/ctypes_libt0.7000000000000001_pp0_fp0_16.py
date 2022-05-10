import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

import datetime
now = datetime.datetime.now()
print now
print now.year
print now.month
print now.day

import os
print os.getcwd()
print os.listdir(".")

import shutil
shutil.copy("test.txt", "test2.txt")

import tempfile
tempfile.gettempdir()

import time
time.time()

import urllib
webpage = urllib.urlopen("http://www.google.com")
print webpage.read()

import xmlrpclib
server = xmlrpclib.Server("http://example.com/RPC2")
server.echo("Hello, World!")

import zipfile
zip = zipfile.ZipFile("test.zip", "w")
zip.write("test.txt")
zip.close()

import PyQt4
import Tkinter
import wxPython

print "Done"
