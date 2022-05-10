import signal
signal.signal(signal.SIGINT, signal_handler)

# Create application instance
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

###############################################################################
#
#  ROUTES
#
###############################################################################
@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/favicon.ico')
def favicon():
    """Renders a sample page."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/v1/echo')
def api_echo():
    """Renders a sample page."""
    return "echo"

