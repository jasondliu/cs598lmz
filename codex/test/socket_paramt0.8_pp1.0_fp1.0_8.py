import socket
socket.if_indextoname(3)

import urllib.request
import urllib.parse
import urllib.error
fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print(line.strip())
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)

import urllib.request
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
