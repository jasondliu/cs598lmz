import types
types.ModuleType.__repr__ = lambda self: self.__name__

# Make sure that __file__ is defined for all modules
import sys
for k,v in sys.modules.items():
    if not hasattr(v, '__file__') and hasattr(v, '__path__'):
        v.__file__ = v.__path__[0] + os.sep + '__init__.py'
    if not hasattr(v, '__file__'):
        v.__file__ = '<builtin>'


import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
logging.info('Logging started')

import pyparsing
pyparsing.ParserElement.enablePackrat()

import pypy.translator.goal.targetnumpypystandalone
import pypy.translator.goal.ann
