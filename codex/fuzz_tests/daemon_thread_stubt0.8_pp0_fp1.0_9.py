import sys, threading

def run():
    server = WSGIServer(("127.0.0.1", 5000), app, log=sys.stdout)
    server.serve_forever()

threading.Thread(target=run).start()

from subprocess import call
while True:
    call(["coffee", "-o", "static/js/", "-w", "coffee/"])
    call(["sass", "sass:static/css"])
    call(["jade", "-w", "jade/", "-o", "static/", "--pretty"])
