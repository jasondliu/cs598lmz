import threading
threading.Thread

# 线程操作
keyWord = "可乐"
#price = 1.6
price = 1.4
while True:
    curPrice = float(getPrice(keyWord))
    print("price====" + str(curPrice))
    if curPrice <= price:
        print("火速抢购")
        os.system('C:\\Users\\Administrator\\Desktop\\可乐.lnk')
        break
    sleep(1)
