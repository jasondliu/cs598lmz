import threading
threading.stack_size(2**27)

try:
    import pygame
except:
    print('installing pygame')
    os.system('pip install pygame')
try:
    import pygame
except:
    print('failed')
    sys.exit(1)

import json
import urllib
import urllib.request
# import os
# import random


def display(game_title, subtitles, options_list):
    global textRect
    global count
    global keynumber
    global k
    global game_title_display
    global game_options_display
    global game_subtitles_display
    global list_of_key_times
    global page
    global page_size
    global page_limit
    global total_pages
    global remaining_page_count
    global current_page
    global remaining_page_size
    global upcoming_page
    global played_page
    global upcoming_page_size
    # global listMoves
    global gameEngine
    global time
    global timeArray
    global b
    global hrsb

