import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("AMO's CP2! | BLUE TEAM")
print(Fore.BLUE + Style.BRIGHT + '''
             ██████╗██████╗
            ██╔════╝██╔══██╗
            ██║     ██████╔╝
            ██║     ██╔═══╝
            ╚██████╗██║
             ╚═════╝╚═╝
             AMO's CP2!


         BLACK TEAM (1)
         RED TEAM (2)
         YELLOW TEAM (3)
         GREEN TEAM (4)
         CYAN TEAM (5)
         BLUE TEAM (6)
         MAGENTA TEAM (7)
         WHITE TEAM (8)

         9 to Remove Console Colours!
         (To Remove Colours From Java Code)
'''
)
select = int(input(Fore.BLUE + Style.BRIGHT + " Enter number: "))

if select == 1:
    print('\n'+
