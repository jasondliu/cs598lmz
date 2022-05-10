import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Python")

# Variables
sleep_timer = 0.5

# Get the size of the console (windows only)
rows, columns = os.popen('stty size', 'r').read().split()

# clear the screen
os.system('cls' if os.name=='nt' else 'clear')

# Print the ASCII art
print("""
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
