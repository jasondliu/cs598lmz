import select
# Test select.select()

def reader(s):
    while 1:
        data = s.recv(1024)
        if data:
            print "Reading", data
        else:
            break

def writer(s, data):
    while 1:
        print "Sending", data
        s.send(data)
        data = data + data

if __name__ == "__main__":
    r, w = os.pipe()
    r, w = os.fdopen(r,"r"), os.fdopen(w,"w")
    r1, w1 = os.pipe()
    r1, w1 = os.fdopen(r1,"r"), os.fdopen(w1,"w")
    reader_thr = threading.Thread(target=reader, args=(r1,))
    writer_thr = threading.Thread(target=writer, args=(w1, "Spam\n"))
    for thr in reader_thr, writer_thr:
        thr.start()
    while 1:
        rl, wl, el = select.select([
