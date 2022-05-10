import sys, threading

def run():
    grid.seek_next_free()
    grid.current_position.display()

grid = grid.Grid()

pthread = threading.Thread(target=run)

# moving cursor to background
sys.stdout.write("\033[?25l")
sys.stdout.flush()

while True:
    pthread.join()
    read = sys.stdin.read(1)

    if read == "w" or read == "W":
        grid.current_position.up()
    elif read == "s" or read == "S":
        grid.current_position.down()
    elif read == "a" or read == "A":
        grid.current_position.left()
    elif read == "d" or read == "D":
        grid.current_position.right()
    elif read == " ":
        grid.current_position.toggle()
    elif read == "q":
        sys.exit(0)

    pthread = threading.Thread(target=run)
    pthread.start()
