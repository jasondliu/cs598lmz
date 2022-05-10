from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

#%%
import re

pattern = re.compile('^(\\w+)\\s(\\d+)\\s(\\d+)$')
m = pattern.match('foo 123 456')
m.groups()

#%%
import re

pattern = re.compile('^(\\w+)\\s(\\d+)\\s(\\d+)$')
pattern.match('foo 123 456').groups()

#%%
import re

pattern = re.compile('^(\\w+)\\s(\\d+)\\s(\\d+)$')
pattern.match('foo 123 456').groups()

#%%
import re

