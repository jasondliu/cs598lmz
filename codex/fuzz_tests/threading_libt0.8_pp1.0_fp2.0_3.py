import threading
threading.Thread(target=start_server).start()

tb = my_top_block()
tb.start()
tb.wait()
