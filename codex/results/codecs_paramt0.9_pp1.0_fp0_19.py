import codecs
codecs.register_error('unicode_escape', codecs.backslashreplace)
response = urllib2.urlopen('http://www.1177.se/Nyheter--artiklar/Fem-okanade-efter-stort-rioter-i-Malmo/?feed=rss_2.0')
feed=response.read()
feed=feed.decode('unicode_escape')
feed=feed.encode('utf-8')
print feed


# In[ ]:




# In[ ]:
