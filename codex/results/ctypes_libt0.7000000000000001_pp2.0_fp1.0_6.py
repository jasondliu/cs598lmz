import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# 5.3.2 execute a program in a subprocess
subprocess.call('type "data.txt"', shell=True)
subprocess.call('notepad.exe "data.txt"', shell=True)
subprocess.check_call('notepad.exe "data.txt"', shell=True)
subprocess.check_output('notepad.exe "data.txt"', shell=True)

# 5.3.3 communicate with a subprocess
p1 = subprocess.Popen(['cat', 'index.rst'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', '.. literalinclude'], stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen(['cut', '-f', '2', '-d', '"'], stdin=p2.stdout, stdout=subprocess.PIPE)
output = p3.communicate()
print(output)

# 5.3
