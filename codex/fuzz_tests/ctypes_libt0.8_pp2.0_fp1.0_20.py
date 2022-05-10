import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Unpoker")

# Start the game

print("\u001b[2J\u001b[H")
print("\u001b[?25l\u001b[36;1m--- New Game ---\u001b[?25h\n")
play()
quit()
