import threading
threading.Thread(target=self.touch_pad, args=(self,data_queue)).start()

data_queue.put('start')
