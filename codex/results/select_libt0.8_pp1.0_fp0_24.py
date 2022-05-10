import select_options
import global_vars
import tools

from tools import print_heading as ph
from tools import print_line as pl
from tools import print_not_implemented as pni

def handle_accounts(self):
    print "\tManaging Accounts"
    print "\t================="
    print ""
    
    self.print_accounts()
    
    while True:
        print "\nManage Accounts Options:"
        print "1) Create New Account"
        print "2) Edit Existing Account"
        print "3) Delete Existing Account"
        print "4) Back"
        choice = raw_input("Select an option: ")
        
        if int(choice) == 1:
            self.create_account()
        elif int(choice) == 2:
            self.edit_account()
        elif int(choice) == 3:
            self.delete_account()
        elif int(choice) == 4:
            break
        else:
            print "Invalid Option!"

def print_accounts(self):
    
    print_
