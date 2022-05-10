import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

#To exit the program 
inp=input("\nPress enter to exit")
