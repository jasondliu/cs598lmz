import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PornHD-DL by github.com/TheSpeedX")

# Create a new console
os.system('mode con: cols=120 lines=40')

# Get current screen size
rows, columns = os.popen('stty size', 'r').read().split()

# Clear screen
os.system('cls')

# Set console size
os.system('mode con: cols=' + columns + ' lines=' + rows)

# Get current console size
rows, columns = os.popen('stty size', 'r').read().split()

# Center window
os.system('mode con: cols=' + columns + ' lines=' + rows + ' && title PornHD-DL by github.com/TheSpeedX && color 2')

# Create a new console
os.system('mode con: cols=130 lines=10')

# Clear screen
os.system('cls')

# Set console size
os.system('mode con: cols=' + columns + ' lines=' + rows)

# Get current console
