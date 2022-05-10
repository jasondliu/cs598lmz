import types
types.UnicodeType = unicode
types.StringType = str

# read config
config.readfp(open('bibserver.ini'))

# app setup
app = Flask(__name__)
api = Api(app)

# bib server setup
bib = BibServer()

# CORS allow from all
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def index():
    return redirect(config.get('bibserver', 'url'))

class CollectionList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

