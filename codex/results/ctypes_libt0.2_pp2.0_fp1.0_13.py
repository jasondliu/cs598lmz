import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# The first argument is the text to be displayed.
# The second argument is the title of the window.
# The third argument is the type of the message box.
# The fourth argument is the name of the icon.
# The fifth argument is the name of the button.
# The sixth argument is the name of the default button.

# The third argument is the type of the message box.
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | No
# 6 : Cancel | Try Again | Continue

# The fourth argument is the name of the icon.
# 0 : No Icon
# 1 : Critical (a.k.a. “X” or “Exclamation”)
# 2 : Question (a.k.a. “?”)
# 3 : Exclamation (a.k.a. “!”)
# 4 : Information (
