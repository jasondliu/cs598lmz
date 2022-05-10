import threading
threading.stack_size(1024*1024*1024)

# Since we are using the python runtime, we will use a simple HTTP
# server for static files. The following code is taken from the
# Flask quickstart guide.
from flask import Flask, render_template, url_for
app = Flask(__name__)

# This is the URL that will be used to access our application, and
# will be used in the HTML template.
app_url = 'http://%s' % os.environ['CURRENT_APPLICATION_ID']

@app.route('/')
def index():
    # This index() route is used to serve the main index.html file.
    return render_template('index.html', app_url=app_url)

