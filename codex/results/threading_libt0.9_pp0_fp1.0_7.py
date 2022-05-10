import threading
threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

def _quit():
    print('$quit')
    sys.stdout.flush()
    sys.exit(0)


def load(fd):
    return pickle.load(fd)
def read_number():
    return int(input())
def read_word():
    return input()
def write_solution(n):
    print(n)
    sys.stdout.flush()

def main():
    n = read_number()
    a = []
    for i in range(n):
        a.append(read_word().strip())
    answer = ''
    for w in a:
        if len(answer)>0 and answer[-1]==w[0]:
            answer = w + answer
        else:
            answer += w

    write_solution(answer)


#This is to avoid stack overflow issues
threading.Thread(target=main).start()
