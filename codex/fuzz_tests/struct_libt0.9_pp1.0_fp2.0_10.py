import _struct
      
print ts.__dict__

from tiddlyweb.web.negotiate import Negotiate

from tiddlyweb.web.http import HTTP400, HTTP404


class TestSelector(MockParent):
    
    @with_environ({'tiddlyweb.config': {
        'log_level' : 'DEBUG',
        'log_file': 'test.log'},
        'tiddlyweb.query': {'tiddlers': 'carrie'}})
    def test_selector_fails_bad_environ(self):
        #bad environ setup where wiki_name and recipe assumed bad
        self.request = dummy_request()
        self.request.environ['tiddlyweb.config']['server_host'] = {
            'scheme': 'http',
            'host': 'example.com',
            }
        self.request.environ['tiddlyweb.store'] = None #bad 
        self.request.environ['tiddlyweb.wiki_name'] = 'WikiName'#bad 
