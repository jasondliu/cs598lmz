import socket

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--encode', type=str, help='Получение кодов клавиш', metavar='keycode') 
parser.add_argument('-d', '--decode', type=str, help='Получение названия клавиш', metavar='key') 
args = parser.parse_args()

def encode(key):
    if key == 'enter':
        return '<Enter>'
    elif key == 'tab':
        return '<Tab>'
    elif key == 'shift':
        return '<Shift>'
    elif key == 'alt':
        return '<Alt>'
    elif key == 'ctrl':
        return '<Ctrl>'
    elif key == 'delete':
        return '<Del>'
