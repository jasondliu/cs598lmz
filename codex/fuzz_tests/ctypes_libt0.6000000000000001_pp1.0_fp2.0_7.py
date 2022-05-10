import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
 

# You can also use a variable instead of "Your text" for the first parameter.

message = "Your text"
ctypes.windll.user32.MessageBoxW(0, message, "Your title", 1)
 

# Or you can use a variable for the title too.

message = "Your text"
title = "Your title"
ctypes.windll.user32.MessageBoxW(0, message, title, 1)
 

# You can also add a line break by using \n within the quotes.

message = "Line 1\nLine 2"
title = "Your title"
ctypes.windll.user32.MessageBoxW(0, message, title, 1)
