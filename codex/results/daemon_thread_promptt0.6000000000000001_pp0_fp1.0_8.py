import threading
# Test threading daemon

def main():
    while True:
        print("Main thread")
        time.sleep(1)

thread = threading.Thread(target=main, daemon=True)
thread.start()

for _ in range(5):
    print("Main thread")
    time.sleep(1)



# Test threading

def main():
    for _ in range(5):
        print("Main thread")
        time.sleep(1)

thread = threading.Thread(target=main)
thread.start()

for _ in range(5):
    print("Main thread")
    time.sleep(1)



# Test asyncio

async def main():
    for _ in range(5):
        print("Main thread")
        await asyncio.sleep(1)

asyncio.run(main())

for _ in range(5):
    print("Main thread")
    time.sleep(1)
