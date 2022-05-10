import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new window
window = sg.Window('Window Title', default_element_size=(40, 1), auto_size_text=False, auto_size_buttons=False)

