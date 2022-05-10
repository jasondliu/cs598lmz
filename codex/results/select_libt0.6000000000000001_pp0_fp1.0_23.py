import selectors
import sys
import traceback

# Messages
# All messages are in json format
# Message format:
# {
#   "type": <type>,
#   "sender": <sender>,
#   "to": <to>,
#   "data": <data>,
# }

# Message types
# Server to client messages
M_CONNECT_SUCCESS = 0
M_CONNECT_FAILURE = 1
M_GAME_START = 2
M_GAME_END = 3
M_GAME_STATE = 4
M_PLAYER_LEFT = 5

# Client to server messages
M_CONNECT = 6
M_DISCONNECT = 7
M_PLAYER_INFO = 8
M_MOVE = 9

# Move types
M_MOVE_UP = 10
M_MOVE_DOWN = 11
M_MOVE_LEFT = 12
M_MOVE_RIGHT = 13
M_MOVE_STOP = 14


class Client:
    def __init__(self, host, port):
        self.host = host
       
