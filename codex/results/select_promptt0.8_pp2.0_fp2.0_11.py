import select
# Test select.select() is working
readable, writable, exceptional = select.select([sys.stdin], [], [])

# Test connection to the Internet
from urllib2 import urlopen
urlopen("http://www.google.com")

# Test that Flask is installed correctly
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
