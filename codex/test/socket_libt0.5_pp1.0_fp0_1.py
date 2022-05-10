import socket
import threading
import time
import sys
import os
import json
import random
import copy
import math
import re
from collections import defaultdict
from collections import Counter

#global variables
host = "localhost"
port = 9999

#dictionary of all the players
players = {}
#dictionary of all the rooms
rooms = {}
#dictionary of all the items
items = {}
#dictionary of all the NPCs
npcs = {}
#dictionary of all the quests
quests = {}
#dictionary of all the enemies
enemies = {}

#dictionary of all the players who are currently fighting
fighting = {}
#dictionary of all the players who are currently trading
trading = {}

#dictionary of all the players who are currently in a group
groups = {}
#dictionary of all the players who are currently in a party
parties = {}

#dictionary of all the players who are currently in a chat
chats = {}

#dictionary of all the players who are currently in a duel
duels = {}

#dictionary of all the players who are currently
