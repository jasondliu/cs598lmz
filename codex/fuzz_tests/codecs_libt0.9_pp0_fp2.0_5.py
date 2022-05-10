import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app = Flask(__name__)
app.config.from_object(config)


app.register_blueprint(html)
app.register_blueprint(api)
db.init_app(app)
sess = Session()
sess.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# If you want to add a new url, do this here:
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=config.DEBUG
    )
