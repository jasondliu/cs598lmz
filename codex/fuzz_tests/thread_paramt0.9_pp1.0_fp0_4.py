import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()

#Q2) What happens if you replace the number 5 by 0 inside the call of function start?

threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()

#Q3) What happens if you replace the number 5 by -1 inside the call of function start?

threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()

#Q4) What happens if you replace the number 5 by 1 inside the call of function start?

threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()

#Q5) What happens if you remove the line threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()?
#The program will print only "bye" without "hi"

#Q6) What happens if you remove it from the program?
#The program will print only "hi" without "bye"


#e) Consider a program fragment.

from time import
