import _struct
import tempfile

import validictory
from twisted.python import usage
from twisted.internet.defer import inlineCallbacks, returnValue

import txaws.credentials
import txaws.service


class Options(usage.Options):
    optParameters = [
        ("config", "c", "config.json", "Configuration file path"),
    ]



def main(reactor, *argv):
    config, error = load_environment_config()
