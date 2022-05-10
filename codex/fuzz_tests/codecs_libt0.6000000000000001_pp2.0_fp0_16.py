import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.value = 0
        self.data = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == 'value':
                        self.value = value
                        break

    def handle_endtag(self, tag):
        if tag == 'input':
            global balance
            balance = self.value

    def handle_data(self, data):
        self.data = data

def main():
    # open a file
    path = 'C:\\Users\\Ethan\\Documents\\School\\Spring 2016\\CS 3540\\Project 1\\'
    f = codecs.open(path + 'html_data.
