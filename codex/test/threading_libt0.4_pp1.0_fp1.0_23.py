import threading
threading.Thread(target=lambda: subprocess.call(['python', '-m', 'SimpleHTTPServer', '8000'])).start()

# Open the web browser
webbrowser.open('http://localhost:8000/')
