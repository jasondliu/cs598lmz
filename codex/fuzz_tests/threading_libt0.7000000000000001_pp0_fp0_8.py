import threading
threading._DummyThread._Thread__stop = m.__stopthread
#sys.settrace(m.trace_calls)
#sys.settrace(m.trace_calls_and_returns)
#sys.settrace(m.trace_lines)
sys.settrace(m.trace_calls)

import xml.sax
import xml.sax.handler
import pprint

class IdsHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.entries={}
    def startElement(self, name, attrs):
        self.entries[attrs['name']]= attrs['id']

class Ids:
    def __init__(self, idsfilename):
        self.idsHandler = IdsHandler()
        self.idsfile = file(idsfilename, 'r')
        self.parser = xml.sax.make_parser()
        self.parser.setContentHandler(self.idsHandler)
        self.parser.parse(self.idsfile)
        self.idsfile.close()
