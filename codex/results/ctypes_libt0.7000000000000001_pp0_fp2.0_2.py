import ctypes
ctypes.windll.kernel32.SetConsoleTitleA(f'{sys.argv[0]} by Lovelace')

def banner():
    title = '''
       8888888b.  8888888888 8888888b.  8888888b.  
         888  888        888   888   888  888 888 
         888  888        888   888   888  888 888 
         888  888        888   888   888  888 Y8P 
         888  888        888   888   888  888     
         888  888        888   888   888  888     
         888  888        888   888   888  888     
       8888888P" 88888888 888   888 8888888P" 888 
                                                 
                                                 
    '''
    print(f'{Fore.CYAN}{Style.BRIGHT}{title}{Style.RESET_
