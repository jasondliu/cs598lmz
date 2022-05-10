import bz2
bz2_file = bz2.BZ2File('enwiki-latest-pages-articles1.xml-p10p30302.bz2')
print(type(bz2_file))
print(bz2_file.peek())
print(bz2_file.readline())
print(bz2_file.readline())

for line in bz2_file:
  print(line)
  break

#%%
print(bz2_file.readline())
print(bz2_file.readline())

#%%
import gzip
gzip_file = gzip.GzipFile('enwiki-latest-pages-articles1.xml-p10p30302.bz2')
print(type(gzip_file))
print(gzip_file.peek())

#%%
import requests
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(response)

#%%
print(response.content)
print(response.text)

#%%
import urllib.request
