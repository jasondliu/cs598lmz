import codecs
codecs.register_error('strict', codecs.ignore_errors)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attrs:
            if name == 'href' and value.startswith('http://www.baidu.com/link?url='):
                self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'a' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)

def get_url(url):
    try:
        response = urllib2.urlopen(url)
        html = response.read()
       
