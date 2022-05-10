from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(c)

# In[ ]:


a = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
c = BZ2Decompressor().decompress(a)
print(c)

# In[ ]:


def solve(c, a=''):
    if '(' not in c:
        return a + c
    else:
        i = c.find('(')
        j = c.find(')')
        s = c[i+1:j].split('x')
        n = int(s[0])
        r = int(s[1])
        return a + c[:i] + solve(c[j+1:j+n+1]*r, a='') + solve(c[j+n+1:
