import sys, threading
threading.Thread(target=lambda: sys.stdout.write("I " + "am "*13 + "dreaming\n")).start()
threading.Thread(target=lambda: sys.stdout.write("of " + "a "*12 + "white " + "X-mas\n")).start()
threading.Thread(target=lambda: sys.stdout.write("just " + "like" + " the "*8 + "one\n")).start()
threading.Thread(target=lambda: sys.stdout.write("you've " + "all "*4 + "enjoyed" + " once "*2 + "upon\n")).start()
threading.Thread(target=lambda: sys.stdout.write("a "*5 + "time\n")).start()


print("I", "am", "dreaming".upper())
