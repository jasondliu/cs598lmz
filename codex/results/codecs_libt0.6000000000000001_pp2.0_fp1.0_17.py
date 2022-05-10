import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# set up logging
logging.basicConfig(filename='wechat.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

# create the Flask app
app = Flask(__name__)

# -----------------------------------------------------------------------------
#  Flask routes
# -----------------------------------------------------------------------------

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # get the signature, timestamp, and nonce parameters
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')

        # get the token from the config file
        token = app.config['WECHAT_TOKEN']

        # combine the token, timestamp, and nonce
        hash
