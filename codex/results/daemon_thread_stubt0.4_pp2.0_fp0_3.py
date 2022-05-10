import sys, threading

def run():
    global data
    global file
    global lock
    global size
    global count
    global total
    global done
    global bs

    while True:
        lock.acquire()
        if file.closed:
            lock.release()
            break
        if not data:
            lock.release()
            continue
        d = data.pop(0)
        lock.release()
        if not d:
            continue
        total += len(d)
        file.write(d)
        count += 1
        if count == size:
            count = 0
            sys.stdout.write('\r%dMB' % (total/1024/1024))
            sys.stdout.flush()
    done.append(1)

def main():
    global data
    global file
    global lock
    global size
    global count
    global total
    global done
    global bs

    if len(sys.argv) < 4:
        print 'Usage: %s [input file] [output file] [threads]' % sys.argv[0]
        sys
