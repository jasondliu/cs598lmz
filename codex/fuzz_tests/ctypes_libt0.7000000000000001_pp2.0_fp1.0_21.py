import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

print("Welcome to my number guessing game")

while True:

    print("Guess a number between 1 and 100")

    answer = random.randint(1, 100)

    guess = int(input())
    count = 1

    while guess != answer:
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        guess = int(input())
        count += 1

    if guess == answer:
        print("YOU WIN")
        print("It took you", count, "tries")
        print("Would you like to play again? (y/n)")
        playagain = input()
        if playagain == "y":
            continue
        elif playagain == "n":
            break
