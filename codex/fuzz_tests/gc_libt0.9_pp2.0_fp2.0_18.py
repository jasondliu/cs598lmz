import gc, weakref, contextlib
import webview
import imgui

import engine
import temp_save as tempsave
import card as card_module
import gui
import gui_game

import time
window = None
window_id = None

def clear():
    global window, window_id
    window = None
    window_id = None

def set_id(id):
    global window_id
    window_id = id

def window_exists(id):
    global window_id
    return window_id == id

# Mark a whole game session as active. -> set id -> change screens, init etc
def set_window(win):
    global window
    window = win

def get_window():
    global window
    return window


#here is an example of how to "get a card"

def get_card(card_id, locale=gui.current_locale):
    global window
    card = card_module.get(card_id, locale)
    print(card)
    if not window.test_mode:
        card = card.copy()
