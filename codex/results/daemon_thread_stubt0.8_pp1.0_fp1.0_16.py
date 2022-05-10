import sys, threading

def run():
    global _game
    _game.Run()

def main(argv):
    global _game

    _game = Main(argv)
    threading.Thread(target=run).start()
