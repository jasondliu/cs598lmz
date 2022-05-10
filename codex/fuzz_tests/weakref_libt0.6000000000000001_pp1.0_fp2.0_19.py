import weakref
import logging
import logging.handlers
import threading
import socket
import json

# This is the list of all messages that the server can send to the client
server_to_client_messages = ['login_success', 'login_failure', 'get_game_list_success', 'get_game_list_failure', 'create_game_success', 'create_game_failure', 'game_start', 'game_update', 'game_end']

# This is the list of all messages that the client can send to the server
client_to_server_messages = ['login', 'create_game', 'join_game', 'leave_game', 'get_game_list', 'move_left', 'move_right', 'move_up', 'move_down', 'shoot', 'quit']

# This is the list of all messages that the server can send to the client
server_to_client_messages = ['login_success', 'login_failure', 'get_game_list_success', 'get_game_list_failure', 'create_game_success', 'create_game
