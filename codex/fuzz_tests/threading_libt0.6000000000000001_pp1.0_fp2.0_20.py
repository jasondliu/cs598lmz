import threading
threading.Thread(target=run_server, daemon=True).start()

from flask import render_template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
