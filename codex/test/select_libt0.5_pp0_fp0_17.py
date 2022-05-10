import selectors
import socket
import types
import sys
import csv
import pickle
import random
import time
import os
import math

#Global variables
sel = selectors.DefaultSelector()
#List of all the clients
clients = []
#List of all the messages
messages = []
#List of all the users
users = []
#List of all the rooms
rooms = []
#List of all the chatrooms
chatrooms = []
#List of all the rooms
admins = []
#List of all the rooms
banned = []
#List of all the rooms
online = []
#List of all the rooms
online_users = []
#List of all the rooms
chatroom_users = []
#List of all the rooms
chatroom_admins = []
#List of all the rooms
chatroom_banned = []
#List of all the rooms
chatroom_online = []
#List of all the rooms
chatroom_online_users = []
#List of all the rooms
chatroom_messages = []
#List of all the rooms
chatroom_messages_
