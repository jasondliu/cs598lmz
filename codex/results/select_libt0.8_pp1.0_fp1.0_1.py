import select

from parsers.fruits import gamelog_fruit, gamelog_fruit_header
from parsers.trees import gamelog_tree, gamelog_tree_header
from parsers.cards import gamelog_card, gamelog_card_header

from config import MAX_PLAYERS

INCOMING = 'incoming_lines.txt'
OUTGOING = 'outgoing_lines.txt'

def write_lines(data):
    with open(INCOMING, 'ab') as f:
        for d in data:
            f.write((d + '\n').encode('utf-8'))

def read_lines():
    with open(INCOMING, 'rb') as f:
        data = f.readlines()
        if data:
            return [d.decode('utf-8').strip() for d in data]
        else:
            return []

def clear_lines():
    with open(INCOMING, 'w') as f:
        pass

def write_outgoing_line(data):
    with open
