import threading
threading.Thread(target=lambda: os.system('python -m http.server --cgi 8080')).start()
