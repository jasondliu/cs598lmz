import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
#
#
def get_input(text):
    while True:
        try:
            user_input = int(input(text))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input
            break
#
#
def get_input_float(text):
    while True:
        try:
            user_input = float(input(text))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return user_input
            break
#
#
def get_input_string(text):
    while True:
        try:
            user_input = str(input(text))
        except ValueError:
            print("Not a string! Try again.")
            continue
        else:
            return user_input
            break
#
#
