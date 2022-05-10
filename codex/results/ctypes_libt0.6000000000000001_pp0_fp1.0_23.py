import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Lazy Server")

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Banner():
    Clear()
    print('''
\033[1;36m
███████╗██╗  ██╗ █████╗ ██╗     ██╗███╗   ██╗██╗   ██╗██████╗  ██████╗ 
██╔════╝██║  ██║██╔══██╗██║     ██║████╗  ██║╚██╗ ██╔╝██╔══██╗██╔═══██╗
█████╗  ███████║███████║██║     ██║██╔██╗ ██║ ╚████╔╝ ██║  ██║██║   ██║
██
