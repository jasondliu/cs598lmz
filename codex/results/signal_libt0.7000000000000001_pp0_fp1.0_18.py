import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

root = tk.Tk()
root.title("Mandelbrot")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

img = PIL.ImageTk.PhotoImage(
    PIL.Image.new("RGB", (WIDTH, HEIGHT), "white")
)
canvas.create_image((0, 0), anchor=tk.NW, image=img)

def draw():
    img.paste(
        PIL.Image.fromarray(
            np.array(
                m.draw(iterations=200), dtype=np.uint8
            )
        )
    )

draw()

def zoom(event):
    m.zoom(event.x, event.y, 1.2)
    draw()

canvas.bind("<Button-1>", zoom)

def move(event):
    m.move(event.x, event.y)
   
