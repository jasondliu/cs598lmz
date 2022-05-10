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
    if error is not None:
        print error
        return

    options = Options()
    try:
        options.parseOptions(argv[1:])
    except usage.UsageError, error:
        print error
        return

    config, error = load_config_file(options)
    if error is not None:
        print error
        return

    try:
        validictory.validate(config, CONFIG_SCHEMA)
    except validictory.FieldValidationError, error:
        print error
        return

    ec2agent = EC2Agent(config)
    ec2agent.startService()
