import bz2
bz2.decompress("BZh91AY&SY".encode()) #b'BZ'

p = bz2.BZ2Parser() #it's a parser that's used to parse bz2 compressed data
p.parse(b"BZh91AY&SY") #<bz2.BZ2File object at 0x7f10f5de5b70>

from urllib import request
response = request.urlopen("http://www.pythonchallenge.com/pc/def/goo...xml.bz2")
response.read()
bzp = bz2.BZ2Parser()
response.read().decode('utf-8').replace("\n","")


from http import cookies
c = cookies.SimpleCookie()
c["fig"] = "newton"
c["poly"] = "pyramid"
print(c)

for morsel in c.values():
    print(morsel.key)
    print(morsel.value)
    print(morsel.coded_value)

from http.cookies import SimpleCookie

