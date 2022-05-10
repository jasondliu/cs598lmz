import select
# Test select.select() as a way to read from stdin and timeout after 5 seconds
# http://stackoverflow.com/questions/1335507/keyboard-input-with-timeout-in-python
#
# Use the msvcrt module for Windows:
#  http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
#
import msvcrt

#
# Test the msvcrt module on Windows (getch())
#  http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
#
def getch():
    while True:
        if msvcrt.kbhit():
            return msvcrt.getch()
        time.sleep(0.1)

#
# Test the msvcrt module on Windows (getch())
#  http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
