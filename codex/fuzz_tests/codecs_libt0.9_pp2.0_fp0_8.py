import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Same as Google Chrome
CHROME_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

def build_url(root, default_params):
    return lambda **params: root + '?' + urlencode(dict(DEFAULT_PARAMETERS, **default_params, **params))

class AuthError(Exception):
    pass

class Page:
    def __init__(self):
        self.content = None
        self.soup = None

    def __enter__(self):
        return self

    def __exit__(self, *excepts):
        if self.is_json() and self.find("error_code") != 0:
            raise AuthError("Authentification failed")

    def open(self, url, parameters=DEFAULT_PAR
