import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()

with open('test', 'rb') as f:
    print(f.read(len(f.read())))
</code>
Если я пишу число в виде <code>bytes(1)</code> в файл, то оно сохраняется в виде <code>b'1'</code>, то есть в виде байтов. Поэтому когда я меняю 1 на 2, что значит b'2', то есть, если я меняю <code>49</code> на <code>50</code>, то получ
