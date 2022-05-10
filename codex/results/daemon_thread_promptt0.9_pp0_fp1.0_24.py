import threading
# Test threading daemon
run_in_main_thread = True
web_server = None
def run_web_daemon():
    import flask
    from flask import Flask, render_template
    from flask import request

    app = flask.Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    if run_in_main_thread:
        app.run()
    web_server = threading.Thread(target=app.run)
    web_server.start()
    return web_server


if __name__ == '__main__':
    run_web_daemon()
