import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def main():
    # Read input
    numCases = int(input())
    cases = []
    for case in range(numCases):
        cases.append(input())
    # Solve cases
    for case in range(numCases):
        print('Case #{}: {}'.format(case + 1, solve(cases[case])))

def solve(case):
    # Parse case
    case = case.split(' ')
    N = int(case[0])
    M = int(case[1])
    # Solve case
    if N == 1 or M == 1:
        return 'YES'
    if N == 2 and M == 2:
        return 'YES'
    return 'NO'

main()
