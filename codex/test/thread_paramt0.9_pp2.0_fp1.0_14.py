import sys, threading
threading.Thread(target=lambda:sys.stderr.write('\x1b[1;31mGo to "http://{}:{}/" to see your app.\x1b[0m\n'.format(os.getenv('IP','localhost'),int(os.getenv('PORT',8080))))).start()
# This is just to make sure that none of the top-level symbols need to be
# named off of this module in order for them to be imported when we do
# "from ... import *".
from .sql import *
from .users import *
from .plugins import *
from .utils import *
from .stdlib import *
from . import authentication, callback_server, preview, reporting, stdlib
from . import example_app

# This is a specific application called 'app'.
app = reporting.App()
app.mount('/preview/', preview.PreviewApp(app))
app.mount('/auth/', authentication.AuthenticationApp(app))
app.mount('/api/', callback_server.CallbackServerApp(app))

# Register some standard content type that we want to use.
