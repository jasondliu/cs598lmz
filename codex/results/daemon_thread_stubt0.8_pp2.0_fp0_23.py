import sys, threading

def run():
    print("Start")
    time.sleep(1)
    print("End")

# run()

# for _ in range(5):
#     thread = threading.Thread(target=run)
#     thread.start()

# print("Hello!")

# print("done!")


class Bomb(threading.Thread):
    def __init__(self,arg):
        super().__init__()
        self.arg = arg

    def run(self):
        print(self.arg)
        time.sleep(1)
        print("Boom!")

bombs = [Bomb(i) for i in range(5)]

for bomb in bombs:
    bomb.start()

print("Hello!")
