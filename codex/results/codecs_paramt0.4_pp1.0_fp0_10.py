import codecs
codecs.register_error('strict', codecs.ignore_errors)

from twisted.internet import reactor, protocol, defer, task
from twisted.protocols import basic
from twisted.python import log

from txircd.modbase import Command
from txircd.utils import irc_lower, ModeType
from txircd.ircutils import splitMessage, irc_equals

class UserCommand(Command):
    def onUse(self, user, data):
        if "password" in data:
            data["password"] = "*"
        return Command.onUse(self, user, data)

class User(UserCommand):
    def __init__(self, ircd):
        self.ircd = ircd
    
    def parseParams(self, user, params, prefix, tags):
        if len(params) < 4:
            user.sendMessage(irc.ERR_NEEDMOREPARAMS, "USER", "Not enough parameters")
            return None
        if params[0] in self.ircd.userNicks:
            user.sendMessage(irc.ERR_
