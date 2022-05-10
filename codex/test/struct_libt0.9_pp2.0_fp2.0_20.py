import _struct
import urllib.request
import urllib.parse
from resources.lib.libraries import client
from resources.lib.libraries import control


def getDomain():
    try:
        base = _addon.getSetting('base')
        base = 'https://www.solarmovie.kim/' if not base else base
        # base = 'https://watch-online.xyz/' if not base else base
        return base
    except:
        return


