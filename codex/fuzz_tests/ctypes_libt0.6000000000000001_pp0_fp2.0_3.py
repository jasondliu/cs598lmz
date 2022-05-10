import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Main window
main = tk.Tk()
main.title("MyApp")

# Create a container
top_frame = tk.Frame(main)

# Layout the container
top_frame.pack(side="top", fill="both", expand=True)

# Create a canvas in the container
canvas = tk.Canvas(top_frame, borderwidth=0, background="#ffffff")

# Layout the canvas
canvas.pack(side="top", fill="both", expand=True)

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(top_frame, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas, background="#ffffff")
canvas.create_window((4, 4), window=frame, anchor="nw", tags
