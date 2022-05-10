import bz2
bz2_file = bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2')

# In[3]:

import xml.etree.ElementTree as ET

# In[4]:

for event,elem in ET.iterparse(bz2_file, events=('start', 'end', 'start-ns', 'end-ns')):
    print(event)
    print(elem)
    print('---')
    if event == 'end' and elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}page':
        print(elem.find('{http://www.mediawiki.org/xml/export-0.10/}title').text)
        print(elem.find('{http://www.mediawiki.org/xml/export-0.10/}id').text)
        print(elem.find('{http://www.mediawiki.org/xml/export-0.10/}revision').find('{http://www.mediawiki.org/
