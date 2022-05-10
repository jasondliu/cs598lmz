import threading
# Test threading daemon
daemon = threading.Thread(target=delete_words, daemon=True) 
daemon.start()

text = input("write text here: ")

while text != 'end':
    print('Writing, please wait...')
    text = input("write text here: ")


 
#daemon.join(timeout=1)

# The daemon will terminate by itself, no need for joining.
#daemon.join()

print("END")



# When the program exits, Tkinter can’t wait for the file dialog to be closed.
# This causes Python to hang and the script never exits.
# There are two ways to avoid this issue.
# First, pressing Ctrl-C while the program is running cancels out of
# the message box, and lets the program finish normally.
# Second, adding root.destroy() at the end of the script cancels the dialog box
# immediately, and the program finishes.
