import threading
# Test threading daemon. 
t = threading.Thread(target=lambda: print("hi"), daemon=True)
# Test if thread is alive.
t.is_alive()
# Test if main thread is alive.
threading.current_thread().is_alive()
# Run
t.start()
# Exit main thread.
threading.current_thread().exit()
# Exit main thread.
exit()
# Force terminate process. Not guaranteed no system wide damage.
os._exit(1)
# Use this instead.
sys.exit(1)
```

```python
# Test socket with tlsext.
import socket
import ssl
s = socket.create_connection(("pypi.python.org", 443))
ssl_sock = ssl.wrap_socket(s,
                           ssl_version=ssl.PROTOCOL_TLSv1,
                           cert_reqs=ssl.CERT_NONE,
                           ca_certs=None)
print(ssl_sock.version())
# Test urlretrieve.
import urllib.request
