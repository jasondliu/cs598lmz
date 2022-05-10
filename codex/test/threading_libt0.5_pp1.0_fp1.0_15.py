import threading
threading.Thread(target=thread_function, args=[1, 2]).start()

# create the window
window = tkinter.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# create the label
lbl = tkinter.Label(window, text="Hello")
lbl.grid(column=0, row=0)

# create the button
btn = tkinter.Button(window, text="Click Me")
btn.grid(column=1, row=0)

