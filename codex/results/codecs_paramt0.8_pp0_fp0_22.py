import codecs
codecs.register_error('ignore', codecs.lookup('ignore'))

def unquote_plus(value):
    return urllib2.unquote(value)

def oauth_header(consumer, token='', realm=''):
    oauthinfo = dict(oauth.OAuth.__dict__)
    oauthinfo['consumer'] = consumer
    oauthinfo['token'] = token
    header = oauth.OAuth(**oauthinfo).to_header(realm=realm)
    header = unicode(header)
    header = header.replace('OAuth ', 'Authorization: ')
    header = header.replace('"', '\\"')
    return header

class Netflix():
    def __init__(self, consumer, token='', realm='', apikey=''):
        self.consumer = consumer
        self.token = token
        self.realm = realm
        self.apikey = apikey

    def search(self, term, t='catalogTitle'):
        base = 'http://api.netflix.com'
        rest = '/catalog
