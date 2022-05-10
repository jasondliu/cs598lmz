from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwiki-latest-pages-articles1.xml-p10p30302.bz2','rb').read())

#The above code will take a long time to run.
#The code below will take a long time to run.
import bz2
for i in range(1,10):
    file = bz2.BZ2File('enwiki-latest-pages-articles%d.xml-p10p30302.bz2' % i,'rb')
    output = open('enwiki-latest-pages-articles%d.xml' % i,'wb')
    output.write(file.read())
    output.close()
    file.close()

#The code below will take a long time to run.
import bz2
for i in range(1,10):
    file = bz2.BZ2File('enwiki-latest-pages-articles%d.xml-p10p30302.bz2' % i,'rb')
    output = open('enwiki-latest-pages-articles%d.xml' % i,'wb')
