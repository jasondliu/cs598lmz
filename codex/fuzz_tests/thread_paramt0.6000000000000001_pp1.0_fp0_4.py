import sys, threading
threading.Thread(target=lambda:sys.stdout.write("1\n")).start()
threading.Thread(target=lambda:sys.stdout.write("2\n")).start()
threading.Thread(target=lambda:sys.stdout.write("3\n")).start()
threading.Thread(target=lambda:sys.stdout.write("4\n")).start()
threading.Thread(target=lambda:sys.stdout.write("5\n")).start()
threading.Thread(target=lambda:sys.stdout.write("6\n")).start()
threading.Thread(target=lambda:sys.stdout.write("7\n")).start()
threading.Thread(target=lambda:sys.stdout.write("8\n")).start()
threading.Thread(target=lambda:sys.stdout.write("9\n")).start()
threading.Thread(target=lambda:sys.stdout.write("10\n")).start()
threading.Thread(target=lambda:sys.stdout.write("11\n")).start()

