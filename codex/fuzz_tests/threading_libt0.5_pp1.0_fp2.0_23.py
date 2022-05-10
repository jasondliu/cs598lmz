import threading
threading.stack_size(1024*1024*1024)

def read_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def write_output(path, output):
    with open(path, 'w') as f:
        f.write(output)

def compute(lines):
    output = 'Case #1:\n'
    N, J = map(int, lines[0].split())
    for i in range(J):
        coin = '1' + format(i, '0%db' % (N-2)) + '1'
        divisors = []
        for base in range(2, 11):
            number = int(coin, base)
            divisor = find_divisor(number)
            if divisor is None:
                break
            divisors.append(divisor)
        else:
            output += coin + ' ' + ' '.join(map(str, divisors)) + '\n'
    return output

def find_divis
