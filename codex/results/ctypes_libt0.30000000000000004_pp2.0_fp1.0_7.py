import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# The first argument is the handle to the parent window.
# The second argument is the text of the message.
# The third argument is the title of the message box.
# The last argument is the type of the message box.
# The return value is the button that the user clicked.
# The return value is 0 if the user closed the message box without clicking a button.

# The last argument is the type of the message box.
# The following table lists the possible values.

# Value Meaning
# 0 OK
# 1 OK | Cancel
# 2 Abort | Retry | Ignore
# 3 Yes | No | Cancel
# 4 Yes | No
# 5 Retry | No
# 6 Cancel | Try Again | Continue

# The return value is the button that the user clicked.
# The following table lists the possible values.

# Value Meaning
# 1 OK
# 2 Cancel
# 3 Abort
# 4 Retry
# 5 Ignore
# 6 Yes
# 7 No
# 10 Try Again
# 11 Continue
