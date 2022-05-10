import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

url="http://www.autohome.com.cn/china/"
con=urllib.request.urlopen(url).read()
data=con.decode('GB2312')
#print(data)


soup=BeautifulSoup(data,'html.parser')
#print(soup.original_encoding)

#print(soup.prettify())

#print(type(soup))

#print(soup.find_all(href=re.compile('http://www.autohome.com.cn/')))

#print(soup.find_all(href=re.compile('http://www.autohome.com.cn/')))

#print(soup.find_all(href=re.compile('http://www.autohome.com.cn/(\w+)/')))

#print(soup.find_all(href=re.compile('http://www
