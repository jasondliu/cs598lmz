import mmap
from PIL import Image
import subprocess

from authmq import conf
from authmq.common import log

from . import qr2
from .appctl import APPCTL
from .devices import DEVICES


class DoIS(object):
    """
    Integrated with authmq.

    When a client visits 'GET /dois' secure server redirects to this handler.
    The handler sends 'dois <authmq_nonce>' request to authmq process, which
    returns the result of authentication and adds itself to a list of remote
    addresses from which authentication responses can be delivered.
    The remote address is sent as part of HTTP request, assuming client uses
    authmq as a proxy.

    Authentication response is put in authmq_nonce.rsp file.
    DoIS reads the file and returns QR generated from the content.
    """

    def __init__(self, _):
        log('init')
        fpath = os.path.joi
