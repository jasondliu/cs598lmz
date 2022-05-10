import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

#----------------------------------------------------------------------------------
# Create window
w = 800
h = 600
aspect_ratio = float(w)/float(h)

window = pyglet.window.Window(width=w,
                              height=h,
                              caption="Pyglet library")

#----------------------------------------------------------------------------------
# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

#----------------------------------------------------------------------------------

def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        print('Q')
        sys.exit(1)
    elif symbol == pyglet.window.key.LEFT:
        print('left arrow')
    elif symbol == pyglet.window.key.RIGHT:
        print('right arrow')
    elif symbol == pyglet.window.key.ENTER:
        print('enter
