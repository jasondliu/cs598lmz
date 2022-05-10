import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # make ctrl+c work

from tornado.options import define, options, parse_command_line
import logging
logging.getLogger().setLevel(logging.DEBUG)

#setup static file serving
define("static_path", os.path.join(os.path.dirname(__file__), "../static"), help="the static files folder")
define("static_url_prefix", "/static/", help="the static files url prefix")

#setup tornado settings
settings = {}
settings['debug'] = True
settings['static_path'] = options.static_path
settings['template_path'] = settings['static_path']

#setup arouter
from arouter import Router
router = Router(settings)

#setup the tornado http server
from tornado.web import Application
application = Application(router.get_handlers(), **settings)

#import server settings and start the server
from server import settings
application.listen(settings.port, settings.host)

