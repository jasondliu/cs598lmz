import threading
threading.Thread(target=start_server).start()

import requests
print '\ndata:', requests.get('http://localhost:5000/data').text
print '\nhello:',requests.get('http://localhost:5000/hello').text
print '\ntest:',requests.get('http://localhost:5000/test').text
print '\nsdfds:',requests.get('http://localhost:5000/sdfds').text
print '\n1st test:',requests.get('http://localhost:5000').text
