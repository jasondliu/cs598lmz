import codecs
codecs.register_error('surrogate_or_special', codecs.surrogateescape)

from .args import add_args
from .log import logger

from . import context
from . import deploy
from . import init
from . import log
from . import render
from . import run
from . import status
from . import tag
from . import test
from . import version
from . import log
from . import upgrade
from . import seed

import pkg_resources

__version__ = pkg_resources.get_distribution("zenoh").version
__author__ = "sascha.bleidner@gmail.com"

# decorator to add an argument to an argparse.ArgumentParser
def arg(*args, **kwargs):
    def decorator(fct):
        add_args(fct, *args, **kwargs)
        return fct
    return decorator

# decorator to add an optional argument to an argparse.ArgumentParser
def optarg(*args, **kwargs):
    kwargs['flag'] = True
    kwargs['default'] = None
   
