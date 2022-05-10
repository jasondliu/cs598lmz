import codecs
codecs.register_error("strict", codecs.ignore_errors)

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return redirect(url_for('login'))
    return render_template('index.html',
            form = dict(request.form),
            data = dict(request.form))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        passwd = hashlib.sha224(request.form['password']).hexdigest()
        with open(app.config['PASSWD'], "r") as f:
            # the newline ("\n") character at the end of the file may turn into a blank line.
            # make sure the line is not empty when we read it
            user_list = dict([(k, v.strip("\n")) for k, v in [
