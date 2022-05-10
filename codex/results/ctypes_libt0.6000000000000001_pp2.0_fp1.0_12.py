import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# How to get current working directory
os.getcwd()

# How to change current working directory
os.chdir('path')

# How to change directory to parent directory
os.chdir('..')

# How to get current username
os.getlogin()

# How to get current user ID
os.getuid()

# How to get current group ID
os.getgid()

# How to get current process ID
os.getpid()

# How to get parent process ID
os.getppid()

# How to get list of all processes
psutil.pids()

# How to get information about current user
os.getuid()

# How to get information about current user
os.getgid()

# How to get information about current user
os.getlogin()

# How to get current user environment
os.getenv('USERNAME')

# How to get all environment variables
os.environ

# How to use get()
