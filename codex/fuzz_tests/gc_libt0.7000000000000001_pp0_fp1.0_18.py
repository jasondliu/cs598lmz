import gc, weakref, os, sys
from . import git, utils, config, pycompat, encoding, error
from .pycompat import getattr

parsers = {}

def getparser(syntax):
    '''getparser(syntax) -> parser

    Return the parser for the specified file name extension.  Raises
    KeyError if no parser is available for the extension.'''
    try:
        return parsers[syntax]
    except KeyError:
        raise error.ParseError(_("unknown file name extension '%s'") % syntax)

def addparser(syntax, parser):
    '''addparser(syntax, parser) -> parser

    Add a new parser that parses files with the specified extension.'''
    parsers[syntax] = parser
    return parser

def _loadparsers(ui, extensions):
    '''Load extensions.'''
    for name, module in extensions.iteritems():
        ui.debug(' loading %s parser from %s\n' % (name, module))
        __import__(module)

def _findpars
