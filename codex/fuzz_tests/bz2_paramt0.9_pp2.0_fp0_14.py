from bz2 import BZ2Decompressor
BZ2Decompressor

with BZ2File("fasta.bz2", "wb") as fp:
    fp.write("Hello, world!\n")
    fp.write("Hello, world!\n")
fp.close()

with BZ2File("fasta.bz2", "rb") as fp:
    print fp.read()

#%%
import urllib
urllib.urlretrieve("http://people.sc.fsu.edu/~jburkardt/data/bzip2/input.1.bz2")

import urllib2
urllib2.install_opener(urllib2.build_opener(
    urllib2.ProxyHandler({'http': 'http://www.someproxy.com:3128'}),
    urllib2.HTTPHandler)
)

#urllib2.install_opener()

import urllib2
response = urllib2.urlopen('http://google.com/')
html = response.read()
print html




#%%
