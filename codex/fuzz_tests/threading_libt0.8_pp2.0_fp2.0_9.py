import threading
threading.Thread(target=lambda: HttpServer.run()).start()

# running the webapp
app.run(debug = True)
