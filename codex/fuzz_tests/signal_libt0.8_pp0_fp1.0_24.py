import signal
signal.signal(signal.SIGINT, lambda signum, frame: get_input())

input_map = {
    'on': lambda x: 'on',
    'off': lambda x: 'off'
}

status = rnn.get_activation()
print(status.upper(), ' (', end='')
if status == 'on':
    print('\033[0;32m', end='')
elif status == 'off':
    print('\033[0;31m', end='')
else:
    print('\033[0;33m', end='')

print("Press CTRL+C to exit", end='')
print("\033[0m", end='')
print(' )', end='')
print("\n")

while True:
    get_input()
