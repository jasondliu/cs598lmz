import bz2
bz2.decompress(compressed)

import http.client
conn = http.client.HTTPConnection("www.python.org")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.
conn.request("GET", "/index.html")
r1 = conn.getresponse()
while not r1.closed:
    print(r1.read(200))  # 200 bytes
