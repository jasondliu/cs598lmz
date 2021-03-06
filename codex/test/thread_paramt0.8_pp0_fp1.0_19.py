import sys, threading
threading.Thread(target=lambda: (sys.stdout.write('\r'), sys.stdout.flush())).start()

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '-' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)

def init():
    global threads, products, result, begin, end
    
    threads = 10
    products = []
    result = []
    begin = 0
    end = 0
    
