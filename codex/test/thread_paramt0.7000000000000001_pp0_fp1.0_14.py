import sys, threading
threading.Thread(target=lambda: __import__('webbrowser').open('http://localhost:8081/')).start()
