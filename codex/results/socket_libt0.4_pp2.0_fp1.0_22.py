import socket
import sys
import time
import urllib
import urllib2
import xml.dom.minidom

# TODO: get rid of this
import pprint
pp = pprint.PrettyPrinter(indent=4)

import lib.config
import lib.helpers
import lib.logger
import lib.message
import lib.plugin
import lib.request
import lib.response
import lib.template
import lib.user

class Main:
    """Main class for the web server."""

    def __init__(self):
        """Initialise the server."""

        # Initialise the logger
        lib.logger.Logger()

        # Initialise the configuration
        lib.config.Config()

        # Initialise the plugins
        lib.plugin.Plugin()

        # Initialise the users
        lib.user.User()

        # Initialise the templates
        lib.template.Template()

        # Initialise the messages
        lib.message.Message()

        # Initialise the socket
        self.socket = socket.socket(socket.AF_INET, socket.
