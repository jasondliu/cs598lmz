import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Setup controllers
left = Controller(0)
right = Controller(1)

# Setup window
window = Window(title="", width=800, height=600, center=False, visible=True)
keyboard = window.keyboard

# Setup pyglet
pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# Setup label
label = pyglet.text.Label(
    "",
    font_name='Consolas',
    font_size=12,
    x=0, y=0,
    anchor_x='left', anchor_y='bottom'
)

# Setup background
background = pyglet.resource.image("background.png")

# Setup box
box = pyglet.resource.image("box.png")
box_pos = [0, 0]

# Setup player
player_image = pyglet.resource.image("player.png")
player_pos = [20, 20]

