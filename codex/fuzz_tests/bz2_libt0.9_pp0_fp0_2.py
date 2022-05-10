import bz2
bz2.decompress(m).decode()

# Give the image below, which identifies the frequency of each crystal used to make the snowflake.
with open('channel/100.txt.bz2') as f:
    for i in range(20):
        f.readline()
    print(''.join(chr(int(k)) for k in f.readline().split()))

# Find the rare characters in the mess below: equality
with open('channel/90052.txt.bz2') as f:
    next_nothing = f.readline()[16:].rstrip()
    f.close()
    while True:
        with open('channel/%s.txt.bz2' % next_nothing) as f:
            content = f.readline()
            f.close()
            print(content)
            if 'Next nothing is' not in content:
                break
            next_nothing = content[16:]
            next_nothing = next_nothing if next_nothing.isdigit() else '8022'

# Can you find the hidden message in the image
