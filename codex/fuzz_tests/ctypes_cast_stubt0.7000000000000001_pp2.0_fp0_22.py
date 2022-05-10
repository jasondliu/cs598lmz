import ctypes
ctypes.cast(0, ctypes.py_object)

# one-liner to get the size of the current screen
w, h = pyautogui.size()

# get a screenshot
im = pyautogui.screenshot()

# shows the screenshot of the screen
im.show()

# save the screenshot to a file, can be one of these formats:
# JPEG, PNG, BMP, TIFF, GIF
im.save('screen_capture.png')

# move the mouse to the center of the screen
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.linear)

# move the mouse to the relative position of the screen
# move mouse 100 pixels right and 100 pixels down
pyautogui.moveRel(100, 100, duration=2, tween=pyautogui.easeInOutQuad)

# get the current mouse position
x, y = pyautogui.position()

# move the mouse to the position of (100, 100)
pyautogui.moveTo(100, 100, duration=2,
