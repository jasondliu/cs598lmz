import ctypes
ctypes.windll.user32.LockWorkStation()
'''

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Start the menu

path = 'my-command'
path2 = 'my-result'

def main_navigation_menu():
    print("Welcome")
    print("This is the navigation menu")
    print("Press q to Exit")


    while True:
        command_menu = raw_input('''
        a: view a list of commands
        b: view history of entered commands
        c: enter a new command
        d: view results of given command

        Please enter a choice: ''')

        if command_menu == 'a':
            view_commands()
        elif command_menu == 'b':
            command_history()
        elif command_menu == 'c':
            add_command()
        elif command_menu == 'd':
            view_results()
        elif command_menu == 'q':
            sys.exit()
        else:
