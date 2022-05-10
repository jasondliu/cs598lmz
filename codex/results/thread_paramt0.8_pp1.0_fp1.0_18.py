import sys, threading
threading.Thread(target=lambda: util.start_gui(sys.argv[1:])).start()

^
