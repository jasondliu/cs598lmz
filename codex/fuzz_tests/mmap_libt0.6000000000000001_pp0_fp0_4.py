import mmap
import re
import sys

from . import __version__
from . import config
from . import log
from . import util
from . import errors
from . import pubkey
from . import keystore
from . import resources


def _json_hook(json_dict):
    """
    json hook that converts "_class" fields into objects
    """
    if '_class' not in json_dict:
        return json_dict
    class_name = json_dict['_class']
    if class_name == 'Address':
        return Address.from_json(json_dict)
    if class_name == 'Wallet':
        return Wallet.from_json(json_dict)
    return json_dict


def json_decode(s):
    """
    Decode JSON data.
    """
    return json.loads(s, object_hook=_json_hook)


def json_encode(obj):
    """
    Encode an object as JSON data.
    """
    return json.dumps(obj, indent=4, default=lambda obj: obj.json())
