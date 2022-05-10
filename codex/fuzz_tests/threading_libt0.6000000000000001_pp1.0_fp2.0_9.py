import threading
threading.Thread(target=app.run, kwargs=dict(host='0.0.0.0', port=5000, debug=True)).start()

# app.run(host='0.0.0.0', port=5000, debug=True)
