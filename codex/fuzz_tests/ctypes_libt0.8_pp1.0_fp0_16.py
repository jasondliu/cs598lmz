import ctypes
ctypes.windll.user32.MessageBoxW(
    0,
    "Hello World!",
    "Title",
    1
)
