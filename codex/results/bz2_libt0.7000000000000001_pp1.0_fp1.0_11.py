import bz2
bz2.decompress("".join(open("python.bz2").readlines()))

#question 10
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
zipfile.ZipFile("channel.zip").extractall()

#question 11
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import zipfile
zipfile.ZipFile("channel.zip").extractall()
nothing=90052
f=open("90052.txt")
s=f.read()
print re.findall("Next nothing is (\d+)",s)[0]
f.close()
while s!="":
    f=open("%d.txt"%nothing)
    s=f.read()
    print re.findall("Next nothing is (\d+)",s)
    print s
    if len(re.findall("Next nothing is (\d+)",s))==0:
        break
    nothing=re.findall("Next nothing is (\d+)
