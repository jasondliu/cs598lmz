import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        _, keepfile = sys.argv
    else:
        keepfile = 'keep.txt'

    dict_keep = {}
    with open(keepfile, 'r') as f:
        for line in f:
            dict_keep[line.strip()] = 1

    while True:
        time.sleep(1)
        pidlist = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        for i in pidlist:
            if i in dict_keep:
                continue
            with open(os.path.join('/proc/', i, 'cmdline'), 'r') as f:
                try:
                    line = f.readline().strip()
                except:
                    continue
                line = line.replace('\0', ' ')
                if line.find('python') != -1:
                    print
