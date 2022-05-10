import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys
import types

import datetime

import rdflib
import rdflib.plugins.sparql.processor

import pytz

import rdflib_jsonld

# Set the default timezone to UTC
try:
    import settings
    if settings.TIME_ZONE:
        os.environ['TZ'] = settings.TIME_ZONE
except (ImportError, AttributeError):
    pass
pytz.timezone('UTC')

try:
    basestring
except NameError:
    basestring = str

# Fix SPARQL result encoding issues.

def _json_encoder_patch(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, (types.GeneratorType, types.FunctionType, types.MethodType, types.BuiltinFunctionType)):
        return str(obj
