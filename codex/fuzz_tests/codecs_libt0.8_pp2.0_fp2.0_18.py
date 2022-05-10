import codecs
codecs.register(lambda x: codec_lookup('utf_8')(x, errors='ignore'))


@app.route('/')
def index():
    return render_template(
        "index.html"
    )


@app.route('/kanjipad')
def kanjipad():
    return render_template(
        "kanjipad.html"
    )


@app.route('/api/kanji/<text>')
def api_get_kanji(text):
    if text is None:
        return Response(json.dumps([])), 200
    text = unquote_plus(text)
    c = KANJI_COLLECTION.find(
        {
            'kanji': {'$regex': re.compile(text, re.UNICODE)}
        }
    ).sort('kanji').limit(2000)
    return Response(dumps(c)), 200


@app.route('/kanji/<text>', methods=['GET'])
def get_kanji(text):
    if text
