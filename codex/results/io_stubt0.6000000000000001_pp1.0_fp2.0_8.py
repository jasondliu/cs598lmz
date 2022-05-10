import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

print(view)

#import os

#print(os.read(0, 1))
#from os import *
#print(read(0, 1))

#import sys
#print(sys.stdin.read(1))
#from sys import stdin
#print(stdin.read(1))

#from sys import stdin
#print(stdin.read(1))

#from sys import *
#print(stdin.read(1))

#from sys import stdin
#print(stdin.read(1))

#import sys
#print(sys.stdin.read(1))
#from sys import stdin
#print(stdin.read(1))

#import sys
#from sys import stdin
#print(stdin.read(1))

#from sys import stdin
#import sys
#print(stdin.read(1))

#from sys import *
#print(stdin.read(1))

#import sys
#from sys import *
#print(stdin.read(1))

