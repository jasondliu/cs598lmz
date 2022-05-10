import threading
threading.stack_size(2**27)
#Replace <YourUserName> with your username
sys.path.insert(0,'/home/<YourUserName>/app')

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
