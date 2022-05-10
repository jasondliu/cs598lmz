fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def hello():
    return 'hi'


def ping():
    return 'pong'


class MyApp(Application):

    def __init__(self):
        self.index_html = '''<html>
            <head><title>Test</title></head>
            <body>
            <h1>Testing <a href="foo/">Foo</a> and <a href="bar/">Bar</a></h1>
            <h2><a href="ping/">ping</a></h2>
            <h2><a href="hello/">hello</a></h2>
            <h2><a href="crash/">crash</a></h2>
            <h2><a href="host/foo/">host</a></h2>
            <h2><a href="exception_in_new/">exception_in_new</a></h2>
            <h2><a href="exception_in_run/">exception_in_run</a></h2>
            <h2><a href="ex
