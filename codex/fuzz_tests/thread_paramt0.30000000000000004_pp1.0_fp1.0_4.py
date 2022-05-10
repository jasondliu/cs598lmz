import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

# sys.stdout.write('\a')

# import os
# os.system('echo -n "\a"')

# import winsound
# winsound.Beep(1000, 1000)

# import subprocess
# subprocess.Popen(['start', 'beep.wav'], shell=True)

# import winsound
# winsound.MessageBeep()

# import ctypes
# ctypes.windll.user32.MessageBeep(-1)

# import winsound
# winsound.PlaySound('beep.wav', winsound.SND_FILENAME)

# import winsound
# winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)

# import winsound
# winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)

# import winsound
# winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

# import winsound
# winsound.PlaySound('SystemExit',
