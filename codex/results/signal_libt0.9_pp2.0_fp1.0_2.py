import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Plugin(BasePlugin):
    __name__ = 'ipb'
    __title__ = 'In-Page Bootstrap'
    __version__ = '1.0.1'
    __description__ = 'Generates in-page bootstrap information.'
    __author__ = 'Wijnand Modderman <maze@pyth0n.org'
    __email__ = 'maze@pyth0n.org'
    __license__ = 'GNU GPLv3'
    events = ('enumerate', 'scandone')


    def enumerate(self, url, ipaddress):
        if url.netloc not in self.ips.keys():
            targets = set()

            # Try to find valid ip addresses in the HTML.
            try:
                r = requests.get(url.geturl())
            except Exception:
                print_exc()
                return
            else:
                page = IPBPage(r.text, url)
                ips = page.find_ips()
