import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create the main window
root = Tk()
root.title("Paint")

# Create the main canvas
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Create the left frame
left = Frame(root, width=200, height=600)
left.pack(side="left", fill="y")

# Create the right frame
right = Frame(root, width=600, height=600)
right.pack(side="right", fill="both", expand=1)

# Create the right-top frame
right_top = Frame(right, width=600, height=450)
right_top.pack(side="top", fill="both", expand=1)

# Create the right-bottom frame
right_bottom = Frame(right, width=600, height=150)
right_bottom.pack(side="bottom", fill="x")

# Create the canvas for the color
color_canvas = Canvas(left,
