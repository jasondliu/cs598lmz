import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("KeySpy")

# -------------------------
# Startup of the programm
# -------------------------

# Set the default values
keylist = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keylist.append(char)

# Create a new window
root = tk.Tk()
root.geometry("500x400")

# Create a new text area
text_area = tk.Text(root)
text_area.pack()

# Make a border around the text area
text_area.config(highlightbackground="black")
text_area.config(highlightthickness=1)

# Create a function for tracking keys
def on_key_press(event):
    # if the key is pressed, append it to the output
    key = event.keysym

    if key == "Return":
        text_area.insert("end", "\n")
    elif key == "BackSpace":
        text_
