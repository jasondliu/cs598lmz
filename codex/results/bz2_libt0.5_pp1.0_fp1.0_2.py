import bz2
bz2.BZ2File('sample.bz2').read()

import zipfile
zipfile.ZipFile('sample.zip').read('sample.txt')

# Chapter 13: Network and Web Programming

# 13.1 Internet Address Lookup

import socket
socket.gethostbyname('www.python.org')
socket.gethostbyname('localhost')
socket.gethostbyaddr('127.0.0.1')

# 13.2 TCP/IP Client and Server

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_
