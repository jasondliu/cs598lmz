import sys, threading

def run():
    while True:
        try:
            print(next(text_to_speech))
        except StopIteration:
            print("end")
            break

text_to_speech = read_text_to_speech(sys.argv[1])

t = threading.Thread(target=run)
t.start()

while True:
    print(next(text_to_speech))
