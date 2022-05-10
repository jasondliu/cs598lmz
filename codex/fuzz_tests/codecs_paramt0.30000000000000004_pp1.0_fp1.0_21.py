import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(filename):
    with open(filename, 'rb') as f:
        return f.read().decode('utf-8', 'strict')

def get_text_from_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8', 'strict')

def get_text_from_url_with_headers(url, headers):
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req).read().decode('utf-8', 'strict')

def get_text_from_url_with_auth(url, username, password):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
   
