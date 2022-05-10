import sys, threading

def run():
    cmd = 'python3 -m http.server {}'.format(SERVER_PORT)
    os.system(cmd)

# Starting up Flask
app = Flask(__name__)

# Starting up the server thread
t = threading.Thread(target=run)
t.daemon = True
t.start()

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=APP_PORT)
