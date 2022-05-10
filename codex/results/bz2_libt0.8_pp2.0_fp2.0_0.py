import bz2
bz2.decompress(f.read())
import gzip
gzip.decompress(f.read())

import sys
print(sys.argv)

import requests
requests.get("http://www.google.com")



"""
print("Enter your name")
x = input()
print("Hello, "+x)
"""


"""
import keyword
print(keyword.iskeyword("False"))
print(keyword.iskeyword("class"))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("return"))
print(keyword.iskeyword("access"))
"""

"""
import sys
while(True):
    print("Enter your name")
    x = sys.stdin.readline()
    if(len(x)<2):
        break
    print("Hello "+x)
"""


"""
import sys
while(True):
    print("Enter your name")
    x = input()
    if(len(x)<2):
        break
    print("Hello "+x)
"""


