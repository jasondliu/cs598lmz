import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
"""
STANDARD_BUTTON_STYLE = sg.BUTTON_TYPE_CLOSES_WIN


def add_button(button_element, name, button_type='OK'):
    """Adds a button to the passed-in button_element.

    Keyword arguments:
    button_element -- The Button Element to the Button to.
    name -- The Text to display on the Button.
    button_type -- The type of Button. Use 'OK', 'Cancel', or 'Exit' for the buttons to close the window.
    """
    container = sg.Frame('', button_element)
    button = [sg.Button(name, size=(14, 1), button_color=('white', 'blue'))]
    if button_type == 'Exit':
        button[0].bind('<Button-1>', close_window)
    container.append_to_frame(button)
    return container

def close_window(event):
    """Closes the Window."""
