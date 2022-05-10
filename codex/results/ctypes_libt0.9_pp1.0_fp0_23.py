import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\Flenn\Downloads\x.png")
</code>
But the image ends up being extremely distorted and it's really obvious that it's not a static image (but rather the Windows background with a static image on top).
How can I achieve what I want with Python?
I'm not very experienced in Python, but any help would be appreciated!

