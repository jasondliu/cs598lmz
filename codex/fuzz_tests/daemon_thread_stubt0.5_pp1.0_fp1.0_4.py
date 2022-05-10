import sys, threading

def run():
    global p
    p = subprocess.Popen(['python3', '-m', 'http.server', '--cgi'], cwd=cgi_dir)

server_thread = threading.Thread(target=run)
server_thread.start()

print('Starting server for %s on port %s ... ' % (cgi_dir, port), end='', flush=True)
while True:
    return_code = p.poll()
    if return_code is None:
        print('done')
        break
    else:
        print('failed')
        sys.exit(return_code)

webbrowser.open('http://localhost:%s/cgi-bin/hello_get.py' % port)
input('Press enter when done...')
p.terminate()
server_thread.join()
