import sys, threading

def run():
    global scanner
    global parser
    global logger
    global currentPlayer
    global currentTurn
    global players
    global turnNum
    global roundNum
    global maxRounds
    global board
    global firstCall
    global server
    global args
    global boardLock
    global loggerLock

    args = parse_input()
    pid = 0

    # initialize
    (scanner, parser, logger, server) = init_server(args)
    (players, maxRounds, board, boardLock, loggerLock, pid) = init_game(args, parser, logger, scanner)

    for i in range(1, maxRounds + 1):
        if firstCall == True:
            firstCall = False
        else:
            msg = {}
            msg['round'] = i
            msg['msg'] = END_MSG
            msg['errors'] = []
            logger.message(msg)

        #play a single round
        roundNum = i
        (result, reason) = play_round(players, board)

        if result == 1:
            msg = {}
            msg['round
