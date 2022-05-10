import signal
signal.signal(signal.SIGINT, signal_handler)

urls = (
        "/", "index",
        "/resources", "resources",
        "/test", "test"
        )

class index:
    def GET(self):
        print "inside index.GET"
        print request.get_vars
        print request.headers
        return "hello"

class resources:
    def GET(self):
        print "inside resources.GET"
        print request.get_vars
        print request.headers
        return "hello"

class test:
    def GET(self):
        print "inside test.GET"
        print request.get_vars
        print request.headers
        return "hello"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
