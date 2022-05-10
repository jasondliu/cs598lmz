import io
# Test io.RawIOBase which calls readline
class TSR(io.RawIOBase):
    def readline(self):
        return 'Foo'
httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
url = 'http://%s:%s/' % (httpd.server_name, httpd.server_port)
test = """import httplib
conn = httplib.HTTPConnection("%s")
conn.request("GET", "/")
""" % httpd.server_name
# Test basic IOBase.readline(), which calls read
open('test.py', 'wt').write(test)
import test
conn = test.conn
r = conn.getresponse()
# Test RawIOBase.readline()
r.isclosed()
r.readline()
r.readline()
r.readline()
r.isclosed()
conn.close()
# Test IOBase.read(), which calls close
# httplib._cs_socket.HTTPResponse.read() doesn't call read() unless it needs
# more data.
import httplib
conn =
