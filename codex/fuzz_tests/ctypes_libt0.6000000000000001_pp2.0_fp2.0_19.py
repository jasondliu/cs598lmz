import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Forcing Tkinter to use DPI scaling
# Make sure to set the DPI scaling to "System" (default) in your computer settings.
# High-DPI scaling down is not supported by Tkinter.
# You may also have to restart your computer for this to work.
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
os.environ['QT_SCALE_FACTOR'] = '1'

# This is for fixing the Tkinter bug which makes the window too small
# on some high-DPI screens.
# It may not be necessary on your computer.
# If you don't need it, comment it out.
os.environ['QT_SCREEN_SCALE_FACTORS'] = '1'

# This is for fixing the Tkinter bug which makes the window too small
# on some high-DPI screens.
# It may not be necessary on your computer.
# If you don't need it, comment it out.
os
