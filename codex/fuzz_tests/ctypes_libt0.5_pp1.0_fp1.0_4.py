import ctypes
ctypes.windll.user32.MessageBoxW(None, "Your text", "Your title", 1)


def main():
    # Get current screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width/2) - (WIDTH/2)
    y = (screen_height/2) - (HEIGHT/2)
    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

    # Set window title
    root.title("Batch Rename")

    # Create the main container
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Create a Tkinter variable
    tkvar =
