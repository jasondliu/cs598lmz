from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(x)

#%%
#3
import re
#findall
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.findall(text)
#match
m = datepat.match('11/27/2012')
m
#groups
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()
month, day, year = m.groups()
text
datepat.findall(text)
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

#%%
#4
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
m

