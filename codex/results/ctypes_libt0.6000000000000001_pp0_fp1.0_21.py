import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# To launch a process and wait for it to finish:
# import subprocess
# subprocess.call("C:\Windows\System32\notepad.exe")

# To launch a process and continue to run your program:
# import subprocess
# subprocess.Popen("C:\Windows\System32\notepad.exe")

# To get the current time:
# import datetime
# datetime.datetime.now()

# To get the current time in a different timezone:
# import datetime
# import pytz
# datetime.datetime.now(pytz.timezone("America/Los_Angeles"))

# To convert a datetime object to a string:
# import datetime
# datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# To convert a string to a datetime object:
# import datetime
# datetime.datetime.strptime("2010-05-07", "%Y-%m-%d")

#
