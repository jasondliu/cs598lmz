from bz2 import BZ2Decompressor
BZ2Decompressor

from lxml import etree

from lxml.etree import XMLParser
parser = XMLParser(huge_tree=True)

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post_index():
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('get_index', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <
