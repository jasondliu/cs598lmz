import select
# Test select.select()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.5)

# Main program
while True:
    slowprint('What is your name?')
    name = raw_input()

    slowprint('Hello, %s.' % name)
    if name.lower() == 'tobi':
        with open('tobi.jpg', 'rb') as f:
            image = f.read()
        slowprint(image)
        break

    slowprint('Are you sure, %s?' % name)
    answer = raw_input()
    if answer.lower() in ('y', 'yes'):
        break
    slowprint('I see.')
