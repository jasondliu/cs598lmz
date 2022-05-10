import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Create the main window
window = tk.Tk()
window.title("Selection")
window.geometry("800x400")

# Create a frame to hold the widgets
frame = tk.Frame(window)
frame.pack()

# Create a menu bar
menubar = tk.Menu(window)

# Create a menu item "File" and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Create a menu item "Help" and add it to the menu bar
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# Display the menu bar
window.config(menu=men
