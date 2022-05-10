import bz2
bz2_data = bz2.BZ2File('data.json.bz2')
data = [json.loads(line) for line in bz2_data]
 
# print the first review
pprint.pprint(data[0])

#project gutenberg
import requests
url = "http://www.gutenberg.org/cache/epub/feeds/rdf-files.tar.bz2"
response = requests.get(url)
with open("rdf-files.tar.bz2", "wb") as file:
    file.write(response.content)
#import tarfile
import tarfile
tar = tarfile.open("rdf-files.tar.bz2", "r:bz2")
tar.extractall()
tar.close()

#web scraping
import requests
from lxml import html
url = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"
response = requests.get(url)
print(response.status
