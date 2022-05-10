from bz2 import BZ2Decompressor
BZ2Decompressor()

#print(soup.prettify())

#soup.prettify()

print(soup.title)

new = soup.select('title')
#print(new)

for i in new:
    print(i.get_text()) 



a_tags = soup.find_all('a')
#print(a_tags)

for link in a_tags:
    print(link.get('href'))
