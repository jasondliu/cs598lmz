import codecs
codecs.register_error('strict', codecs.ignore_errors)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_link = False
        self.data = []
        self.pages = []
        self.count = 0
        self.next_page = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.in_link = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_link = False

    def handle_data(self, data):
        if self.in_link:
            self.data.append(data)
            self.count += 1
            if self.count == 2:
                self.pages.append(data)
                self.count = 0
                

def get_list(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data = response.read()
    encoding =
