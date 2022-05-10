import threading
threading.Thread(target=input).start()
#
# Set up a window
#
win = visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False)

#
# Draw two objects to the window
#
obj1 = visual.Rect(win, width=200, height=200, fillColor='red')
obj2 = visual.Rect(win, width=200, height=200, fillColor='blue')

#
# Draw the stimuli and update the window
#
for frameN in range(10):
    obj1.draw()
    obj2.draw()
    win.flip()

#
# These lines are necessary for some platforms
# for proper closing of the window.
#
win.winHandle.activate()
while win.winHandle.get_key() != 'escape':
    pass
win.close()
core.quit()
