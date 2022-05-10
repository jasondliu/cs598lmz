import threading
threading.stack_size(102400)

def _get_data():
    # 获取数据
    data=[]
    for i in range(10000):
        data.append(i)
    return data

def _get_result(data,q):
    # 计算数据
    result = []
    for i in data:
        result.append(i**2)
    # 将计算结果放入队列
    q.put(result)

def _main():
    data = _get_data()
    q = Queue()
    # 开启多线程
    t1 = threading.Thread(target=_get_result, args=(data[:5000],q))
    t2 = threading.Thread(target=_get_result, args=(data[5000:],q))
    t1.start()
    t2.start()
    # 获取结
