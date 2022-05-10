import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

# Get the member list from the site
memberList = []

def getHTML(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
    response = urlopen(req)
    html = response.read()
    response.close()
    return str(html)

def getAllMember(url):
    html = getHTML(url)
    bs = BeautifulSoup(html, "lxml")
    table = bs.findAll('table')[1]
    rows = table.findAll('tr')
    for row in rows:
        cols = row.
