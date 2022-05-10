import selectors
import types
from urllib.parse import urlparse

sel = selectors.DefaultSelector()


def fetch(url):
    o = urlparse(url)
    conn = http.client.HTTPConnection(o.netloc)
    conn.request('GET', o.path)
    resp = conn.getresponse()
    print(resp.status, resp.reason)
    body = resp.read()
    print(body)
    # conn.close()


def fetch_async(url):
    o = urlparse(url)
    conn = http.client.HTTPConnection(o.netloc)

    req = conn.request('GET', o.path)

    def read_response(conn, mask):
        # print(req.getresponse())
        print(conn.getresponse().read())
        # sel.unregister(conn)
        # conn.close()

    sel.register(conn, selectors.EVENT_READ, read_response)


def loop():
    while True:
        events = sel.select()
        for key,
