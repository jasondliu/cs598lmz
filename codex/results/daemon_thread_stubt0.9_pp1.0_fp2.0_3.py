import sys, threading

def run():
    sys.path.insert(0, 'C:\\My\\Repos\\python\\brewitup')
    from web.app import app as application

threading.Thread(target=run).start()

env = bootstrap.make_load_environment()
application = dispatcher.load_wsgi_application()
</code>
I've seached around a bit and many have suggested using WSGIScriptAlias to load the application from a separate file, but I'd prefer not to do that. What I would like is to have my wsgi wrapped within a bootstrap object that can be dynamically loaded when I restart wsgi by flushing the process's code cache. Can I do this with mod_wsgi?


A:

What you want to do I think is possible, but you need to be passing in the application object directly to mod_wsgi. That is, start the application in a background thread and then pass its WSGI application object to mod_wsgi via a WSGI application script.
You can only start mod_wsgi via a WSGI script file however, so that is where you need to put the top level of your code.

