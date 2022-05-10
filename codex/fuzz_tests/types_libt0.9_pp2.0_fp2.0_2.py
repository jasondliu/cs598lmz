import types
types.FunctionType
import sys

from lib import app_helper
from lib.app_helper import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xdd\xc4\xce\xe4\x9b\xbf\xd5_\xf5\x1d\x13\xbd4\x18\xc4\x9b\x95\xd5\xcc\xfa&\xacfp\x1f&'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'flask_sid'
app.config['PERMANENT_SESSION_LIFETIME'] = 86400

files = UploadSet('files', ALL) 
configure_uploads(app, files)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():

	if request.method == 'POST':
		
