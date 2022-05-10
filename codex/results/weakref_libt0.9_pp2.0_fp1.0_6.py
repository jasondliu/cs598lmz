import weakref

CLIENT_ID = u"sVNKOcgJ84"
CLIENT_SECRET = u"uIb6FeT7rGKyH24Dg7vYGd6UiAzfGrj3"
TOKEN = u"WLHlKT9hx2xRLDvDP8kltbtARU6hFw6ChyE6KT8e"

COLOR_ARRAY = np.array(Image.open("assets/colors.png"), dtype=np.uint8)

class DisplayingHandler(BaseHTTPRequestHandler):
    def __init__(self, *a, **k):
        BaseHTTPRequestHandler.__init__(self, *a, **k)

    def log_message(self, format, *args):
        pass
        
    def do_GET(self):
        if self.path == '/favicon.ico':
            return
        
        result = self.server.get_json()
        self.getResponse(result)
            
    def getResponse(self, result):
        result_json
