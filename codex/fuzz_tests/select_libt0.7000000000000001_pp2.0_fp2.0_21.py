import select
import tty
import sys
import json
import time
import os
import threading
import Queue
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from subprocess import call
import random
import socket

# TODO:
# - Add more interaction with objects (e.g. pick up, put down etc.)
# - Add more interaction with entities
# - Add more voice commands
# - Add more responses
# - Add natural language processing
# - Add more things to interact with
# - Add more rooms
# - Add more animations
# - Add rewards
# - Add punishments
# - Add endgame

# Game constants
HOST = 'localhost'
PORT = 50000

# Game variables
game_control = True
game_over = False
game_pause = False
game_speed = 4
game_loop_time = 0.1
game_stage = 1
game_last_voice_command = None
game_last_voice_command_time = 0
game_last_voice_command_repeat = False
game_room = 1
game_room_prev =
