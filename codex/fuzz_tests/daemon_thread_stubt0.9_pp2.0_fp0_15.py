import sys, threading

def run():
    # Get the user input
    print "Enter a decimal number: "
    decimal = float(raw_input())

    # Set the maximum number of iterations
    epsilon = 0.01
    step = epsilon**2
    numGuesses = 0
    answer = 0.0

    # Bisection search
    while abs(answer**2 - decimal) >= epsilon and answer <= decimal:
        answer += step
        numGuesses += 1

    if abs(answer**2 - decimal) >= epsilon:
        print numGuesses, "itr. Last guessed square is", answer
    else:
        print numGuesses, "itr. ", answer, "is close to square root of", decimal

thread = threading.Thread(target = run)
thread.start()
