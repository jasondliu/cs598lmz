import signal
signal.alarm(4)

# Input
name = input("")

# Check
if "Hack" in name:
    print("Good Job")
else:
    print("Try Again")
