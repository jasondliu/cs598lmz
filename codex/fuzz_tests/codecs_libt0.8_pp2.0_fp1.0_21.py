import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# ========================
# Routes
# ========================
ROUTES = [
    ('/api/lists', ListEndpointHandler)
]
