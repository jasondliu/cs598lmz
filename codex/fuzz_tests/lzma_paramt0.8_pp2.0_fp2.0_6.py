from lzma import LZMADecompressor
LZMADecompressor().decompress(payload)

```


```py
p = Process(target=foo)
p.start()
# do some other stuff
p.join()

```


```py
@app.route('/typo', methods=['GET', 'POST'])
def typo():
    if request.method == 'POST':
        body = request.get_data()
        user_id,text = body.decode('utf-8').split(' ')
        n = len(text)
        # send message to user_id with input text
        return jsonify({'error': 0, 'n': n})
    else:
        return jsonify({'error': -1})
```


```py
@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return jsonify({'error': -1})
        file = request.files['image']

