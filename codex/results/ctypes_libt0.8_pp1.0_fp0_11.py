import ctypes
ctypes.windll.user32.MessageBoxW(None, "문자열", "제목", 0)

# messagebox.askyesno("제목", "문자열", )


# 0 - OK
# 1 - OK, Cancel
# 2 - Abort, Retry, Ignore
# 3 - Yes, No, Cancel
# 4 - Yes, No
# 5 - Retry, Cancel
# 16 - Critical Message
# 32 - Warning Query
# 48 - Warning Message
# 64 - Information Message
# 0 - Default Button
# 256 - Application Modal
# 512 - System Modal
# 4096 - Task Modal

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()

# messagebox.showinfo("창제목", "확인을누르시면 창이 닫힙니다.")
#
