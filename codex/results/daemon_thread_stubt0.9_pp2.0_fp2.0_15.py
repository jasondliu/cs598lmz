import sys, threading

def run():
    gcd = RPC.Service('gcd')

    while True:
        try:
            print 'Please enter an int:',
            num1 = int(raw_input())
            print 'Please enter an int:',
            num2 = int(raw_input())
            print 'GCD is:', gcd.getGcd(num1, num2)
        except (ValueError, RPC.Error):
            print 'Invalid Number!'
            continue


if __name__ == '__main__':

    threading.Thread(target=run).start()

    s = RPC.Server([RPC.Service('gcd')])
    s.serve()
