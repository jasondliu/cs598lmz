import sys, threading
threading.Thread(target=lambda: sys.stdout.write(start_server())).start()

@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.form:
    #     print(request.form['username'])
    #     print(request.form['password'])
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    return render_template('update.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/signup/submit', methods=['POST'])
def signup_submit():
    if request.form:
        username = request.form['username']
        password = request.form['password']
