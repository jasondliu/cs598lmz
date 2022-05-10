import codecs
codecs.register(codecs.lookup('idna'))
from urllib import urlencode
from urllib2 import urlopen, quote, Request
from commands import Command
import json
from chatbot.config import get_key


class Youtube(Command):

    helptext = "Searches youtube for defined terms, returns link to first result"
    paramre = re.compile("(?:(\S*)\s?)")

    def doCommand(self, message, userterms):
        """message is name of calling user,"""
        if len(userterms) == 0:
            return self._sendMessage("you need to define some search terms")

        query_string = urlencode({"search_query" : quote(" ".join(userterms))})
        html_content = urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode('utf-8'))
        APIKey = get_key("youtube")
        url
