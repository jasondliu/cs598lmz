import threading
# Test threading daemonic mode

def action(i):
    print(i ** 32)


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 32)


if __name__ == '__main__':
    t1 = threading.Thread(target=action, args=(2,))
    t2 = threading.Thread(target=action, args=(3,))
    t3 = threading.Thread(target=action, args=(4,))
    t4 = threading.Thread(target=action, args=(5,))
    t5 = threading.Thread(target=action, args=(6,))
    t6 = threading.Thread(target=action, args=(7,))
    # t1 = threading.Thread(target=Power, args=(2,))
    # t2 = threading.Thread(target=Power, args=(3,))
    # t3 = threading.Thread(target=Power, args=(4,))
    # t4 = threading.Thread(target=
