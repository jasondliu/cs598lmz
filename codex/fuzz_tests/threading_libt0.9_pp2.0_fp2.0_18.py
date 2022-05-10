import threading
threading.Thread(target=self.touch_pad, args=(self,data_queue)).start()

data_queue.put('start')
'''

# ========================= test function ==========================
def test_get_data_from_queue(win_bac):
    print('win_bac=', win_bac)
    print('test_get_data_from_queue: ', data_queue.get())


win_back = Tk()
Button(win_back, text="Stop", command=test_get_data_from_queue(win_back)).pack()

# 按钮
btn_row_1 = [0, 0, 0, 0, 0]
btn_row_2 = [0, 0, 0, 0, 0]
btn_row_3 = [0, 0, 0, 0, 0, 0, 0]

# times
time_row_1 = [0.1, 0.1, 0.1, 0.1, 0.1]
time_row_2 = [0.1, 0.1, 0.1, 0
