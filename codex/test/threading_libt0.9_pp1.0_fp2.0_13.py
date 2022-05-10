import threading
threading.stack_size(67108864)

def digitCancellingFractions(n):
    l = []
    for i in range(1, n):
        for j in range(i+1, n):
            if i < 10 and j < 10:
                continue
            elif i % 10 == 0 or j % 10 == 0:
                continue
            d = set(list(str(i))).intersection(set(list(str(j))))
            if len(d) == 1:
                a = d.pop()
                if a in str(int(i/10)) and a in str(int(j/10)):
                    if j % int(j/10) == 0 and i % int(i/10) == 0:
                        k = j/i
                        jj = int(int(j)/10)
                        ii = int(int(i)/10)
                        l.append((jj, ii))
