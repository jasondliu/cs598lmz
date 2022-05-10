import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

current_reserve = collections.defaultdict(int)

def fund(name, exchange):
    cls = getattr(__import__("main.exchanges"), exchange)
    if not exchange.startswith("Local"):
        while current_reserve[exchange] &gt; 0:  # block until fully reserved
            time.sleep(1e-3)
    with cls._mutex:
        cls._fund_map[name] += 1000

def reserve(exchange, amount):
    current_reserve[exchange] += amount

def main():
    work = [
        (fund, "btcusd", "Gemini",),
        (fund, "btcusd", "Bitfinex",),
        (fund, "btcusd", "Bitfinex",),
        (fund, "golem-usd", "Gemini",),
        (fund, "go
