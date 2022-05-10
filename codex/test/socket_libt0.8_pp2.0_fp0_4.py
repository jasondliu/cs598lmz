import socket
import time
import re


class Bot:

    nick = "G.N.O.M.E"
    chan = "#bot_ranch"
    ircServ = "irc.gamesurge.net"
    port = 6667
    #ircServ = "irc.freenode.org"
    #port = 6001
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cmd_delay = 1.5
    time_last = 0.0
    chanconlist = {"k1ll3r1"}
    
    def connect(self):
        print("Connecting to " + self.ircServ + " on port " + str(self.port))
        self.irc.connect((self.ircServ, self.port))
        self.irc.send("USER " + self.nick + " " + self.nick + " " + self.nick + " :I'm a Bot!\n")
        self.irc.send("NICK " + self.nick + "\n")
