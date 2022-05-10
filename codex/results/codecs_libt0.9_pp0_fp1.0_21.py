import codecs
codecs.BOM_UTF16

# -*- coding: utf-8 -*-
u'Ⅲ'

u'\u2162'

 
s = u'Ⅲ'.encode('utf-8')
print(s)
print(type(s))
print(s.decode('utf8'))
print(type(s.decode('utf8')))


# In[ ]:
