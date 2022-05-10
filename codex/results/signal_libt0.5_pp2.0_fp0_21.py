import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# New imports added for the tkinter GUI
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Import the backend
import backend

# Create a window
window = tk.Tk()
window.title("Book Store")
window.geometry("640x480")

# Create a label for the title of the window
label_title = ttk.Label(window, text="Book Store", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2)

# Create a label for the title of the books
label_title = ttk.Label(window, text="Title")
label_title.grid(row=1, column=0)

# Create a label for the author of the books
label_author = ttk.Label(window, text="Author")
label_author.grid(row=1, column=2)

# Create a label for the year of the books
label
