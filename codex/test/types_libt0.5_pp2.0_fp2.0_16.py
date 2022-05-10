import types
types.MethodType(get_text, None, BeautifulSoup)

def get_text(self):
    return re.sub("\s+", " ", self.decode_contents())

BeautifulSoup.get_text = get_text

#get all the urls of the threads in a given web page
def get_thread_urls(url):
    #connect to a URL
    website = urlopen(url)

    #read html code
    html = website.read()

    #use re.findall to get all the links
    links = re.findall('"((http)s?://.*?)"', html.decode('utf-8'))

    #filter out the links that are not the threads
    thread_urls = []
    for link in links:
        if "thread" in link[0]:
            thread_urls.append(link[0])

    return thread_urls

#get all the urls of the threads in a given web page
