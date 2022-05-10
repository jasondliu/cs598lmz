import bz2
bz2file = bz2.open('data/dumps/enwiki-latest-pages-articles1.xml-p10p30302.bz2')
for line in bz2file: 
    text = line
    break
text

#%%
import wikitextparser as wtp
page = wtp.parse(text)
#print(page.extract_links())
[link for link in page.extract_links() if ':' not in link] # filter out all links containing a colon

#%%
import vcr

#%%
with vcr.use_cassette('data/dumps/enwiki-latest-pages-articles1.xml-p10p30302.bz2.yml'):
    # with vcr.use_cassette('data/dumps/enwiki-latest-pages-articles1.xml-p10p30302.bz2.yml', filter_headers=['cookie']):
    requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = requests.get
