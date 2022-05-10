from bz2 import BZ2Decompressor
BZ2Decompressor()

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado import gen
from tornado.httpclient import AsyncHTTPClient



class MainHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        content = yield AsyncHTTPClient().fetch(
            "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2")
        yield gen.sleep(0.1)
        self.write(content.body)


application = Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    IOLoop.instance().start()
