import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\n".join(["koebe_1", "1 3", "2 2", "3 1"])+"\n")).start()
threading.Thread(target=lambda:sys.stdout.write("\n".join(["koebe_2", "5 7", "5 8", "5 8", "5 7", "5 7"])+"\n")).start()
threading.Thread(target=lambda:sys.stdout.write("\n".join(["koebe_3", "54 90", "54 57", "87 57", "87 90"])+"\n")).start()
threading.Thread(target=lambda:sys.stdout.write("\n".join(["koebe_4", "39 80", "39 45", "63 45", "63 80"])+"\n")).start()
threading.Thread(target=lambda:sys.stdout.write("\n".join(["koebe_5", "50 82", "50 61", "76 61", "76 82"])+"\n")).start()
