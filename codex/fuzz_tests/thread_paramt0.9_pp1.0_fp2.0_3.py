import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1B[31m> red text\x1B[0m\n")).start()
 
# Orrrrr with Lambda (for SFW reddit):
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1B[31m> red text\x1B[0m\n")).start()
 
# Orrrr with Lambda + split (for SFW reddit):
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1B[31m> red text\x1B[0m\n".split(" ")[1])).start()
 
# Orrrr with Lambda + split + format (for SFW reddit):
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1B[31m> red text\x1B[0m\n".split(" ")[1].replace("\x1B[31m> red text\x1B[0m\n", ""))
