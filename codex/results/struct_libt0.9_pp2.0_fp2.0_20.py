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


def getSoup(url, data=None):
    try:
        headers = {}

        if '|' in url:
            url, agent = url.split('|')
            headers['User-Agent'] = agent

        if data != None and 'http://' in url:
            data = urllib.parse.urlencode(data)
            data = data.encode('utf-8')
            result = client.request(url, post=data, headers=headers)
        else:
            result = client.request(url, headers=headers)

        return BeautifulSoup(result)
    except:
