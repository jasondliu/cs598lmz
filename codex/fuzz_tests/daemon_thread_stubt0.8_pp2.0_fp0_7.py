import sys, threading

def run():
    while True:
        prompt = '&gt; '
        command = input(prompt)
        print(command)

def print_some_text():
    print("some text\n")

threading.Thread(target=run).start()

while True:
    print_some_text()
</code>

