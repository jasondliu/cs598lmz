import socket
socket.if_indextoname()
 
import sys
print(sys.getwindowsversion())
```
* Print Version
```python
import sys
# Using with sys
print(sys.version)
import platform
# Using with platform
print(platform.python_version())
```

### Library
* Requests
```python
import requests
resp = requests.get(url)
print(resp.headers['Content-Type']) # application/json; charset=utf-8

resp = requests.post(url, json={'data':'test'})
print(resp.text)

resp = requests.post(url, files={'file': open('file.txt', 'rb')})
print(resp.text)

resp = requests.post(url, files={'file': ('test.txt', 'sth...')})
print(resp.text)

resp = requests.post(url, files={'file': ('test.png', open('img.png', 'rb'), 'img/png')})
print(resp.text)

resp = requests.post(url, files={'file': ('
