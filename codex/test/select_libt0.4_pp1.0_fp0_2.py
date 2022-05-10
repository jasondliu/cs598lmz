import select

def main():
    s = socket.socket()
    s.bind(('0.0.0.0', 5000))
    s.listen(5)
    inputs = [s]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is s:
                c, addr = s.accept()
