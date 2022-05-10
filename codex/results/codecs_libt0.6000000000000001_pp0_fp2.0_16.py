import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.secret_key = 'development key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        # Parse form data
        email = request.form['email']
        username = request.form['username']
        passwd = request.form['password']
        passwd2
