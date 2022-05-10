import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

l = []
with open('sample_data.csv', 'r', encoding='utf-8') as reader:
    for row in reader:
        l.append(row.strip().split(','))

l = map(lambda i: i.split(','), open('sample_data.csv'))
</code>

