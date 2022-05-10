import sys, threading

def run():
    subprocess.run([sys.executable, '-m', 'http.server', '8000'], cwd='./dist')

threading.Thread(target=run).start()

# The same run as before, but a new thread is spawned to run the server
# Since pytest waits until the test function is done running, it doesn't
# matter that our http server is still running when we exit.
</code>

