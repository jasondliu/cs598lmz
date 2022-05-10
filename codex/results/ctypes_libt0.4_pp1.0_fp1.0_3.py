import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

# https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
# https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list
