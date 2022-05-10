import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


def center_window(window, width=300, height=200):
    """
    centers a tkinter window
    :param window: the root or Toplevel window to center
    """
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def get_running_button():
    with open('running_button.txt', 'r') as f:
        running_button = f.readline()
        return running_button


def get_shortcut_button(shortcut):
    with open('buttons.txt', 'r') as f:
        lines = f.readlines()

