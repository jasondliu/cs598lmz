import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from twisted.internet import reactor
from twisted.words.protocols import irc
from twisted.web import xmlrpc,server

cfg={}

try:
	from time import timezone
except ImportError:
	timezone=0

def handle_INVITE(self, user, channel):
	"""
	Handles INVITE
	"""
	user=user.split('!',1)[0]
	if not self.master:
		if self.factory.allow_invites:
			self.join(channel)
			self.msg(channel,"Hello, "+user+". I am a bot in testing. I am at your service.")
			self.msg(channel,"If you want to control me, send me a private message with the password. If you need help, send me a private message with the command HELP.")
			self.msg(channel,"If you have a suggestion or a comment, send it to qa@zombofant.net.")
		
