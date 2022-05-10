import threading
threading.stack_size(1024*1024)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(f)

    print('filename: ' + file.filename)

    thread = threading.Thread(target=classify_process, args=(f,))
    thread.start()

    return render_template('index.html')

def classify_process(filename):
    result = app.clf.classify(filename)
    print('result: ' + result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
