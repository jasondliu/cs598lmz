import sys, threading

def run():
    board = SendBoard()
    board.init_board()
    board.make_pre_board()
    board.start_server()
    board.run_board()
    board.end_board()

run()
