import sys, threading

def run():
    global t1, t2, i
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.bind(('localhost', 8000))
    con.listen(5)

    while True:
        rd, wr, er = select.select([con], [], [])
        for r in rd:
            if r is con:
                # Accept connection
                con2, rem = con.accept()
                rd.append(con2)
            elif r is con2:
                # Get data
                data = r.recv(1024)
                if data:
                    print("Data: " + data)
                    # Parse data and reply
                    if data == '1':
                        r.send("OK1")
                    elif data == '2':
                        r.send("OK2")
                    else:
                        r.send("WHAT")
        if i == 0:
            return

def main():
    global t1, t2, i
    i = 1
    t1 = threading.Thread(target=run
