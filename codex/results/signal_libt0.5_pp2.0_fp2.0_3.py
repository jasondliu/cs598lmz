import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the application.
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/websocket", WebSocketHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static/"}),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
