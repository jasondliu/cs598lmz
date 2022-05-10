import select
# Test select.select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

inputs = [s]
outputs = []

while True:
    r, w, e = select.select(inputs, outputs, inputs)
    print("r:", r)
    print("w:", w)
    print("e:", e)
    
    for s in r:
        if s is s:
            conn, addr = s.accept()
            print("Got connection from", addr)
            inputs.append(conn)
        else:
            data = s.recv(1024)
