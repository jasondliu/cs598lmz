import codecs
codecs.register(lambda encoding=_encoding: codecs.lookup(_encoding) if encoding == "utf-8" else None)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
