import codecs
codecs.register_error("strict", codecs.replace_errors)

# A class to parse incoming from mIRC
class LogParser(object):
    def __init__(self, source, destination, default_nick, default_ident, default_hostname):
        self.source = source
        self.destination = destination
        self.re = re.compile("^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] <(.+)> (.+)$")
        self.default_nick = default_nick
        self.default_ident = default_ident
        self.default_hostname = default_hostname
        self.timeformat = "%Y-%m-%d %H:%M:%S"
        self.timestring = "%Y-%m-%d %H:%M:%S"

    def parse(self, line):
        # Parse [date] <nick> message
        match = self.re.match(line)

        if not match:
            return None

        nickname
